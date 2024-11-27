
export default {
  bootstrap: () => import('./main.server.mjs').then(m => m.default),
  inlineCriticalCss: true,
  routes: [
  {
    "renderMode": 2,
    "route": "/"
  }
],
  assets: new Map([
['index.csr.html', {size: 512, hash: '480046ad7fe318cb7fb79a5cd1daf291d728e09db8359ca81b75729f4d5ab597', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)}], 
['index.server.html', {size: 1025, hash: '957175d7b8ab2d583645cdd71f7ca54b9b744ad672e5576afac2b6c548e3ce40', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)}], 
['index.html', {size: 20847, hash: '40f24ea5628f5260f87d1d66e7ad4087f45323114a69829e2d90326368bd16e0', text: () => import('./assets-chunks/index_html.mjs').then(m => m.default)}], 
['styles-5INURTSO.css', {size: 0, hash: 'menYUTfbRu8', text: () => import('./assets-chunks/styles-5INURTSO_css.mjs').then(m => m.default)}]
]),
  locale: undefined,
};
