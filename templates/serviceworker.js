const y = new Date().getFullYear();
const m = new Date().getMonth();
const d = new Date().getDate();
const h = new Date().getHours();
/*
  Com o cache com esse nome, o SW tentará atualizar o cache a cada hora.
*/
const CACHE_NAME = 'bqm-cache-v' + y + m + d + h;
/*
  Se definico como true, o sw tentará atualizar a lista de cache cosntantemente, e não a cada hora.
*/
const DEBUG = false;
/*
  Arquivos essenciais a serem colocados e cache.
*/
var urlsToCache = [
  '/',
  '/app.js',
  '/manifest.json',
  '/media/video.webm',
  '/media/maskable_icon_x48.png',
  '/media/maskable_icon_x72.png',
  '/media/maskable_icon_x96.png',
  '/media/maskable_icon_x128.png',
  '/media/maskable_icon_x144.png',
  '/media/maskable_icon_x152.png',
  '/media/maskable_icon_x192.png',
  '/media/maskable_icon_x256.png',
  '/media/maskable_icon_x384.png',
  '/media/maskable_icon_x512.png',
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
/*
  Intala o Sw no dispositivo do usuário, criando um cache de dos arquivos essenciais.
*/
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
    /*
      Filtra os caches com prefixo bqm-cache-, e apaga as versoes anteriores do cache salvo.
    */
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
  /*
    verifica se e uma solicitação da API, se for, o SW não irá buscar no cache.
  */
  if(!event.request.url.includes('/api/')) {
    /*
      Se não for a pagina de log off
    */
    if(!event.request.url.includes('/sair/')) {
      /*
        Sempre que for uma solicitação da lib mathjax, incluir o resultado em cache.
        Pode-se fazer isso pois esta não se altera.
      */
      if(event.request.url.includes('/mathjax/')) {
        event.respondWith(
            caches.match(event.request).then(response => {
              return response || fetch(event.request).then((response) => {
                let responseClone = response.clone();
                caches.open(CACHE_NAME).then((cache) => {
                  cache.put(event.request, responseClone);
                });
                return response;
              });
            }).catch(() => {
              return caches.match('/offline/');
            })
        );
      } else {
        /*
          Sempre que for um arquivo de media, incluir no cache.
        */
        if(event.request.url.includes('/media/')) {
          event.respondWith(
              caches.match(event.request).then(response => {
                return response || fetch(event.request).then((response) => {
                  let responseClone = response.clone();
                  caches.open(CACHE_NAME).then((cache) => {
                    cache.put(event.request, responseClone);
                  });
                  return response;
                });
              }).catch(() => {
                return caches.match('/offline/');
              })
          );
        } else {
          /*
            Tenta buscar os arquivos em cache, se não encontrar, tenta buscar na rede
            se não conseguir conectar na rede, exibe uma pagina de offline
          */
          event.respondWith(
              caches.match(event.request).then(response => {
                return response || fetch(event.request);
              }).catch(() => {
                return caches.match('/offline/');
              })
          );
          /*
            Sempre que algun dos arquivos guardados em cache for chamado, se possivel, o SW 
            tentará atualizar o arquivo no cache.
            Só tem efeito se a variavel DEBUG for true, se ela for false, o cache 
            será atualizado a cada hora, pelo evento activate
          */
          if (DEBUG) {
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
        }
      }
    } else {
      /*
        Se for a pagia de logoff, sempre buscar na rede
      */
      event.respondWith(
        fetch(event.request)
      )
    }
  } else {
    /*
      Busca um arquivo na rede sempre que for uma solicitacao da API
    */
    event.respondWith(
      fetch(event.request)
    )
  }
});
/*
  Forca a atualização de um dado arquilo listado no cache.
  E mais utilizado quando o DEBUg = true
*/
function update(request) {
  return fetch(request.url).then(response => {
    if (!response.ok) {
      throw new Error('Não foi possivel conectar ao url');
    } else {
      return caches.open(CACHE_NAME).then(cache => cache.put(request, response.clone())).then(() => response)
    }
  })
}
/*
  Tenta garantir que os arquivos de cache sempre estarao atualizados.
*/
self.addEventListener('sync', function(event) {
  if (event.tag == 'cache') {
    if (DEBUG) {
      event.waitUntil(
        caches.open(CACHE_NAME)
        .then(cache => {
            return cache.addAll(urlsToCache);
        })
      )
    }
  }
});
