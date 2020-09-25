window.$('DIV#toggle_header').click(() => {
  if (window.$('HEADER').hasClass('red')) {
    window.$('HEADER').removeClass('red');
    window.$('HEADER').addClass('green');
  } else if (window.$('HEADER').hasClass('green')) {
    window.$('HEADER').removeClass('green');
    window.$('HEADER').addClass('red');
  }
});
