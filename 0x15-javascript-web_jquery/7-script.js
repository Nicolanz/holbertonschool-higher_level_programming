window.$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
  window.$('DIV#character').text(data.name);
});
