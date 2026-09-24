/* Offline cache for 실기퀴즈.
 * Pages, CSS and JS are network-first so a new deploy reaches returning
 * visitors on their next online visit; images and fonts are cache-first.
 */
const CACHE_NAME = 'eip-quiz-v3';
const PRECACHE = [
  './',
  './index.html',
  './style.css',
  './quiz.js',
  './java.html',
  './python.html',
  './c.html',
  './sql.html',
  './network.html',
  './os.html',
  './software-engineering.html',
  './db.html',
  './algorithm.html',
  './uml.html',
  './newtech.html',
  './integration.html',
  './img/hero-decks.webp',
  './img/empty-ring.webp',
  './icons/icon-192.svg',
  './icons/icon-512.svg'
];

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(PRECACHE)));
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

function isFreshFirst(request) {
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return false;
  return request.mode === 'navigate' || /\.(html|css|js)$/.test(url.pathname) || url.pathname.endsWith('/');
}

async function networkFirst(request) {
  const cache = await caches.open(CACHE_NAME);
  try {
    const response = await fetch(request);
    if (response.ok) cache.put(request, response.clone());
    return response;
  } catch (err) {
    const cached = await cache.match(request, { ignoreSearch: true });
    if (cached) return cached;
    if (request.mode === 'navigate') {
      const fallback = await cache.match('./index.html');
      if (fallback) return fallback;
    }
    throw err;
  }
}

async function cacheFirst(request) {
  const cached = await caches.match(request);
  if (cached) return cached;
  const response = await fetch(request);
  if (response.ok || response.type === 'opaque') {
    const cache = await caches.open(CACHE_NAME);
    cache.put(request, response.clone());
  }
  return response;
}

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  event.respondWith(isFreshFirst(event.request) ? networkFirst(event.request) : cacheFirst(event.request));
});
