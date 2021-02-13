if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('https://bq.mat.br/sw.js', { scope: '/' }).then(function(registration) {
      if(registration.installing) {
        console.log('Service worker installing');
      } else if(registration.waiting) {
        console.log('Service worker installed');
      } else if(registration.active) {
        console.log('Service worker active');
        /*
          Se o dispositivo suportar o SyncManager, registrar uma siscronizacao chamada cache
        */
        if ('SyncManager' in window) {
          navigator.serviceWorker.ready.then(function(swr) {
            return swr.sync.register('cache');
          });
        }
      }
  }).catch(function(error) {
      console.log('Registration sw failed with ' + error);
  });
}
