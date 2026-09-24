/* 정보처리기사 실기 퀴즈 — shared page behavior.
 * Grades live only in this browser (localStorage). No network calls.
 */
(function () {
  'use strict';

  var STORE_KEY = 'eip-quiz:v1';
  var LEGACY_KEYS = { sql: 'sql-quiz-progress', python: 'python-quiz-progress' };

  var DECKS = [
    { id: 'java', name: 'Java', total: 10 },
    { id: 'python', name: 'Python', total: 10 },
    { id: 'c', name: 'C언어', total: 10 },
    { id: 'algorithm', name: '알고리즘', total: 10 },
    { id: 'sql', name: 'SQL', total: 10 },
    { id: 'db', name: 'DB설계', total: 10 },
    { id: 'network', name: '네트워크', total: 10 },
    { id: 'os', name: '운영체제', total: 10 },
    { id: 'software-engineering', name: '소프트웨어공학', total: 10 },
    { id: 'uml', name: 'UML', total: 10 },
    { id: 'newtech', name: '신기술', total: 10 },
    { id: 'integration', name: '모의고사', total: 20 }
  ];

  var memoryStore = null; // used when localStorage is unavailable (private mode, blocked storage)

  function emptyStore() { return { v: 1, decks: {}, last: null, migrated: {} }; }

  function readStore() {
    if (memoryStore) return memoryStore;
    try {
      var raw = window.localStorage.getItem(STORE_KEY);
      var data = raw ? JSON.parse(raw) : emptyStore();
      if (!data || typeof data !== 'object' || !data.decks) data = emptyStore();
      data.migrated = data.migrated || {};
      return data;
    } catch (e) {
      memoryStore = emptyStore();
      notice('이 브라우저에서는 채점 기록을 저장할 수 없어요. 페이지를 닫으면 기록이 사라집니다.');
      return memoryStore;
    }
  }

  function writeStore(data) {
    if (memoryStore) { memoryStore = data; return; }
    try {
      window.localStorage.setItem(STORE_KEY, JSON.stringify(data));
    } catch (e) {
      memoryStore = data;
      notice('채점 기록을 저장하지 못했어요. 저장 공간을 확인해 주세요. 이번 방문 동안은 기록이 유지됩니다.');
    }
  }

  /* Earlier SQL/Python pages stored a "풀이 완료" checkbox per question.
     Carry those over once as 맞음 so nobody loses progress. */
  function migrateLegacy(data) {
    Object.keys(LEGACY_KEYS).forEach(function (deck) {
      if (data.migrated[deck]) return;
      data.migrated[deck] = true;
      try {
        var old = JSON.parse(window.localStorage.getItem(LEGACY_KEYS[deck]) || '{}') || {};
        var grades = data.decks[deck] || {};
        Object.keys(old).forEach(function (q) {
          if (old[q] && !grades[q]) grades[q] = 'right';
        });
        if (Object.keys(grades).length) data.decks[deck] = grades;
      } catch (e) { /* unreadable legacy data is ignored */ }
    });
    return data;
  }

  function deckStats(data, deck) {
    var grades = data.decks[deck.id] || {};
    var right = 0, wrong = 0;
    for (var q = 1; q <= deck.total; q++) {
      if (grades[q] === 'right') right++;
      else if (grades[q] === 'wrong') wrong++;
    }
    return { right: right, wrong: wrong, graded: right + wrong, total: deck.total };
  }

  function firstOpen(data, deck) {
    var grades = data.decks[deck.id] || {};
    for (var q = 1; q <= deck.total; q++) if (!grades[q]) return q;
    return null;
  }

  function findDeck(id) {
    for (var i = 0; i < DECKS.length; i++) if (DECKS[i].id === id) return DECKS[i];
    return null;
  }

  var noticeEl = null;
  function notice(message) {
    if (!document.body) return;
    if (!noticeEl) {
      noticeEl = document.createElement('p');
      noticeEl.className = 'notice';
      noticeEl.setAttribute('role', 'status');
      document.body.insertBefore(noticeEl, document.body.firstChild);
    }
    noticeEl.textContent = message;
  }

  /* ---------- hand-drawn red-pen marks ---------- */
  var MARKS = {
    right: '<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false"><path d="M33 7c-14 0-26 10-26 25 0 14 11 25 25 25 15 0 25-11 25-25C57 18 46 8 31 9" /></svg>',
    wrong: '<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false"><path d="M12 12c13 12 27 26 40 41" /><path d="M52 10C39 24 26 38 11 53" /></svg>'
  };

  /* ---------- nav ---------- */
  function initNav() {
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.getElementById('deck-nav');
    if (!toggle || !nav) return;
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? '과목 메뉴 닫기' : '과목 메뉴 열기');
      nav.classList.toggle('open', open);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.setAttribute('aria-label', '과목 메뉴 열기');
        toggle.focus();
      }
    });
    var current = nav.querySelector('[aria-current="page"]');
    if (current && current.scrollIntoView && window.matchMedia('(min-width: 769px)').matches) {
      nav.scrollLeft = current.offsetLeft - nav.clientWidth / 2 + current.clientWidth / 2;
    }
  }

  /* ---------- deck page ---------- */
  function initDeck(deckId) {
    var deck = findDeck(deckId);
    var cards = Array.prototype.slice.call(document.querySelectorAll('.question-card[data-q]'));
    if (!deck || !cards.length) return;
    deck.total = cards.length;

    var data = migrateLegacy(readStore());
    writeStore(data);

    var tally = document.querySelector('[data-tally]');
    var tallyText = document.querySelector('[data-tally-text]');
    var filterButtons = Array.prototype.slice.call(document.querySelectorAll('[data-filter]'));
    var resetButton = document.querySelector('[data-reset]');
    var filter = 'all';

    var slots = [];
    if (tally) {
      cards.forEach(function (card) {
        var q = card.getAttribute('data-q');
        var a = document.createElement('a');
        a.href = '#q-' + q;
        a.className = 'slot';
        a.tabIndex = -1;
        a.textContent = q;
        tally.appendChild(a);
        slots.push(a);
      });
    }

    var empty = document.createElement('div');
    empty.className = 'empty-state';
    empty.hidden = true;
    empty.innerHTML = '<img src="img/empty-ring.webp" alt="" width="160" height="160" loading="lazy">' +
      '<p class="empty-title"></p><p class="empty-body"></p>' +
      '<button type="button" class="chip-button" data-empty-all>전체 문제 보기</button>';
    var lastCard = cards[cards.length - 1];
    lastCard.parentNode.insertBefore(empty, lastCard.nextSibling);
    empty.querySelector('[data-empty-all]').addEventListener('click', function () { setFilter('all'); });

    cards.forEach(function (card) {
      var q = card.getAttribute('data-q');
      /* multi-line program output (Python, SQL result rows) keeps its line breaks */
      card.querySelectorAll('.answer-value').forEach(function (v) {
        if (v.innerHTML.indexOf('\n') !== -1 && !v.querySelector('br')) v.classList.add('is-pre');
      });
      var header = card.querySelector('.question-header');
      var numEl = card.querySelector('.q-num');
      var mark = document.createElement('span');
      mark.className = 'mark';
      mark.setAttribute('aria-hidden', 'true');
      if (header) header.appendChild(mark);

      var status = document.createElement('span');
      status.className = 'visually-hidden';
      status.setAttribute('data-status', '');
      if (numEl) numEl.appendChild(status);

      var details = card.querySelector('details');
      var answer = card.querySelector('.answer-content');
      if (!details || !answer) return;

      var grade = document.createElement('div');
      grade.className = 'grade';
      grade.setAttribute('role', 'group');
      grade.setAttribute('aria-label', (numEl ? numEl.firstChild.textContent.trim() : '문제 ' + q) + ' 채점');
      grade.innerHTML = '<span class="grade-label">내 답은 어땠나요?</span>' +
        '<button type="button" class="grade-btn" data-grade="right" aria-pressed="false"><span class="grade-glyph">' + MARKS.right + '</span>맞았어요</button>' +
        '<button type="button" class="grade-btn" data-grade="wrong" aria-pressed="false"><span class="grade-glyph">' + MARKS.wrong + '</span>틀렸어요</button>';
      answer.appendChild(grade);

      grade.addEventListener('click', function (e) {
        var btn = e.target.closest('[data-grade]');
        if (!btn) return;
        var value = btn.getAttribute('data-grade');
        var store = readStore();
        var grades = store.decks[deck.id] || {};
        if (grades[q] === value) delete grades[q];
        else grades[q] = value;
        store.decks[deck.id] = grades;
        store.last = { deck: deck.id, q: Number(q), at: Date.now() };
        writeStore(store);
        render(true, q);
      });

      details.addEventListener('toggle', function () {
        if (!details.open) return;
        var store = readStore();
        store.last = { deck: deck.id, q: Number(q), at: Date.now() };
        writeStore(store);
      });
    });

    function setFilter(next) {
      filter = next;
      filterButtons.forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-filter') === next)); });
      var url = new URL(window.location.href);
      if (next === 'all') url.searchParams.delete('filter'); else url.searchParams.set('filter', next);
      window.history.replaceState(null, '', url.pathname + url.search + url.hash);
      render(false);
    }

    filterButtons.forEach(function (b) {
      b.addEventListener('click', function () { setFilter(b.getAttribute('data-filter')); });
    });

    if (resetButton) {
      resetButton.addEventListener('click', function () {
        var s = deckStats(readStore(), deck);
        if (!s.graded) return;
        if (!window.confirm(deck.name + ' 채점 기록 ' + s.graded + '개를 지울까요? 되돌릴 수 없어요.')) return;
        var store = readStore();
        delete store.decks[deck.id];
        writeStore(store);
        cards.forEach(function (c) { var d = c.querySelector('details'); if (d) d.open = false; });
        render(false);
      });
    }

    function render(animate, changedQ) {
      var store = readStore();
      var grades = store.decks[deck.id] || {};
      var s = deckStats(store, deck);
      var shown = 0;
      cards.forEach(function (card, i) {
        var q = card.getAttribute('data-q');
        var g = grades[q] || '';
        card.setAttribute('data-grade', g);
        var mark = card.querySelector('.mark');
        if (mark) {
          mark.innerHTML = g ? MARKS[g] : '';
          mark.classList.toggle('draw', !!(animate && changedQ === q && g));
        }
        var st = card.querySelector('[data-status]');
        if (st) st.textContent = g === 'right' ? ' (맞음)' : g === 'wrong' ? ' (틀림)' : '';
        card.querySelectorAll('[data-grade]').forEach(function (b) {
          if (b === card) return;
          b.setAttribute('aria-pressed', String(b.getAttribute('data-grade') === g));
        });
        if (slots[i]) {
          slots[i].setAttribute('data-grade', g);
        }
        var visible = filter === 'all' || (filter === 'todo' && !g) || (filter === 'wrong' && g === 'wrong');
        card.hidden = !visible;
        if (visible) shown++;
      });
      if (tallyText) {
        tallyText.textContent = s.graded + ' / ' + s.total + ' 채점 · 맞음 ' + s.right + ' · 틀림 ' + s.wrong;
      }
      if (resetButton) resetButton.disabled = s.graded === 0;
      empty.hidden = shown !== 0;
      if (!shown) {
        empty.querySelector('.empty-title').textContent = filter === 'wrong' ? '틀린 문제가 없어요' : '모든 문제를 채점했어요';
        empty.querySelector('.empty-body').textContent = filter === 'wrong'
          ? '채점하면서 “틀렸어요”를 누른 문제가 여기에 모입니다.'
          : '틀린 문제만 다시 풀어 보거나, 다른 과목으로 넘어가 보세요.';
      }
    }

    var initial = new URL(window.location.href).searchParams.get('filter');
    if (initial === 'todo' || initial === 'wrong') setFilter(initial); else render(false);

    window.addEventListener('storage', function (e) { if (e.key === STORE_KEY) render(false); });
  }

  /* ---------- hub ---------- */
  function initHub() {
    var data = migrateLegacy(readStore());
    writeStore(data);
    var totalQ = 0, graded = 0, wrong = 0, worst = null;
    DECKS.forEach(function (deck) {
      var s = deckStats(data, deck);
      totalQ += s.total; graded += s.graded; wrong += s.wrong;
      if (s.wrong && (!worst || s.wrong > worst.wrong)) worst = { deck: deck, wrong: s.wrong };
      var el = document.querySelector('[data-deck-card="' + deck.id + '"]');
      if (!el) return;
      var meter = el.querySelector('[data-deck-meter]');
      if (meter) {
        meter.style.setProperty('--right', (s.right / s.total * 100) + '%');
        meter.style.setProperty('--wrong', (s.wrong / s.total * 100) + '%');
      }
      var label = el.querySelector('[data-deck-progress]');
      if (label) {
        label.textContent = s.graded
          ? s.graded + '/' + s.total + ' 채점' + (s.wrong ? ' · 틀림 ' + s.wrong : '')
          : s.total + '문제';
      }
    });

    var tally = document.querySelector('[data-hub-tally]');
    if (tally) {
      tally.textContent = graded
        ? '전체 ' + totalQ + '문제 중 ' + graded + '문제 채점, 틀린 문제 ' + wrong + '개'
        : '아직 채점한 문제가 없어요. 첫 카드부터 넘겨 보세요.';
    }

    var resume = document.querySelector('[data-resume]');
    if (resume) {
      var target = null;
      if (data.last && findDeck(data.last.deck)) {
        var lastDeck = findDeck(data.last.deck);
        var open = firstOpen(data, lastDeck);
        if (open) target = { deck: lastDeck, q: open };
      }
      if (!target) {
        for (var i = 0; i < DECKS.length && !target; i++) {
          var q = firstOpen(data, DECKS[i]);
          if (q) target = { deck: DECKS[i], q: q };
        }
      }
      if (target) {
        resume.href = target.deck.id + '.html#q-' + target.q;
        resume.querySelector('[data-resume-label]').textContent = (graded || data.last)
          ? '이어서 풀기 · ' + target.deck.name + ' ' + target.q + '번'
          : '첫 문제부터 풀기';
      } else {
        resume.href = 'integration.html';
        resume.querySelector('[data-resume-label]').textContent = '모의고사 다시 풀기';
      }
    }

    var review = document.querySelector('[data-review]');
    if (review) {
      if (worst) {
        review.hidden = false;
        review.href = worst.deck.id + '.html?filter=wrong';
        review.textContent = '틀린 문제 다시 보기 · ' + worst.deck.name + ' ' + worst.wrong + '개';
      } else {
        review.hidden = true;
      }
    }
  }

  function start() {
    initNav();
    var deckId = document.body.getAttribute('data-deck');
    if (deckId) initDeck(deckId);
    else if (document.body.hasAttribute('data-hub')) initHub();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();

  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('./sw.js').catch(function () { /* offline cache is optional */ });
    });
  }

  // exposed for tests only
  window.__quiz = { deckStats: deckStats, firstOpen: firstOpen, migrateLegacy: migrateLegacy, STORE_KEY: STORE_KEY };
})();
