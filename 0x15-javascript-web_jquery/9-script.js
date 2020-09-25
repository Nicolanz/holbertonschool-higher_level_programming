window.$.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  window.$('DIV#hello').text(data.hello);
});
