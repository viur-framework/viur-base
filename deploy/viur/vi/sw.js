self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open('sw-cache').then(function(cache) {
		return cache.addAll([
	      'pyodide.asm.data',
	      'pyodide.asm.wasm',
	      'pyodide.asm.js',
	      'pyodide.asm.data.js',
	      'pyodide.js',
		  'vi.html'
        ])
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});
