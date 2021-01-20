var CACHE_NAME = 'bqm-cache-v' + new Date().getTime();

var urlsToCache = [
  '/',
  '/app.js',
  '/manifest.json',
  '/media/icon48x48px.png',
  '/media/icon72x72px.png',
  '/media/icon96x96px.png',
  '/media/icon128x128px.png',
  '/media/icon144x144px.png',
  '/media/icon152x152px.png',
  '/media/icon192x192px.png',
  '/media/icon256x256px.png',
  '/media/icon384x384px.png',
  '/media/icon512x512px.png',
  '/media/poster.png',
  '/offline/',
  '/politica_de_privacidade/',
  '/sobre/',
  '/static/css/fonts.css',
  '/static/css/reset.css', 
  '/static/css/stylesheet.css', 
  '/static/fonts/Roboto-Regular-webfont.woff',
  '/static/img/grid.png',
  '/static/js/api.js',
  '/static/js/editor.js',
];

self.addEventListener('install', event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                return cache.addAll(urlsToCache);
            })
    )
});


self.addEventListener('activate', event => {
    event.waitUntil(

        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith('bqm-cache-')))
                    .filter(cacheName => (cacheName !== CACHE_NAME))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});


self.addEventListener('fetch', event => {

  if(!event.request.url.includes('/api/')) {

    event.respondWith(
        caches.match(event.request).then(response => {
          return response || fetch(event.request);
        }).catch(() => {
          return caches.match('/offline/');
        })
    );

    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
          cache.keys().then(function (keys) {
              for (var i = 0; i < keys.length; i++) {
                if (event.request.url == keys[i].url) {
                  update(event.request)
                }
              }
          })
        })
    );
    
  }

});


function update(request) {
  return fetch(request.url).then(response => {
    if (!response.ok) {
      throw new Error('Não foi possivel conectar ao url');
    } else {
      return caches.open(CACHE_NAME).then(cache => cache.put(request, response.clone())).then(() => response)
    }
  })
}