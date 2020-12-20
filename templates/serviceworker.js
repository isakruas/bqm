const CACHE_NAME = 'bqm-cache-v1';
const urlsToCache = [

  'https://bq.mat.br/',
  'https://bq.mat.br/sobre/',
  'https://bq.mat.br/politica_de_privacidade/',
  'https://bq.mat.br/ir_para/',

  'https://bq.mat.br/app.js',
  'https://bq.mat.br/sw.js',
  'https://bq.mat.br/manifest.json',

  'https://bq.mat.br/media/offline.html',

  'https://bq.mat.br/static/css/fonts.css',
  'https://bq.mat.br/static/css/reset.css',
  'https://bq.mat.br/static/css/stylesheet.css',
  'https://bq.mat.br/static/fonts/Roboto-Regular-webfont.woff',
  'https://bq.mat.br/static/js/script.js'
]

self.addEventListener('install', function(event){
    event.waitUntil(
        caches.open(CACHE_NAME)
        .then(function(cache){
            //console.log('Opened cache');
            return cache.addAll(urlsToCache)
        })
    );
});

self.addEventListener('fetch', function(event) {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request)
    .then(function(response) {
      return response || fetchAndCache(event.request);
    })
  );
});

function fetchAndCache(url) {
  return fetch(url)
  .then(function(response) {
     
    if (response.type === 'opaqueredirect') {
      return response;
    }

    if (!response.ok) {
      throw Error(response.statusText);
    }

    let ContentType = response.headers.get('Content-Type');

    if (ContentType == 'text/html; charset=utf-8' || ContentType == 'text/html') {
      return response;
    } else {
      return caches.open(CACHE_NAME)
      .then(function(cache) {
        cache.put(url, response.clone());
        return response;
      });
    }

  }).catch(function(error) {
 
    console.log('Request failed:', error);

    

    return caches.match('https://bq.mat.br/media/offline.html');
  });
}

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys
        .filter(function (key) {
          return key.indexOf(CACHE_NAME) !== 0;
        })
        .map(function (key) {
          return caches.delete(key);
        })
      );
    })
  );
});