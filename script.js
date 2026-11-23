// Placeholder links (data-todo) should not jump to the top of the page.
document.querySelectorAll('a[data-todo]').forEach((a) => {
  a.title = 'Link not added yet';
  a.addEventListener('click', (e) => e.preventDefault());
});

// Fade sections in on scroll and highlight the current nav link.
if ('IntersectionObserver' in window) {
  const items = document.querySelectorAll('main section:not(.hero), .card, .pubs li');
  const show = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('in'); show.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px' });
  items.forEach((el) => { el.classList.add('reveal'); show.observe(el); });

  const links = [...document.querySelectorAll('.site-header ul a')];
  const spy = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      links.forEach((a) => a.classList.toggle('active', a.getAttribute('href') === '#' + e.target.id));
    });
  }, { rootMargin: '-30% 0px -60% 0px' });
  document.querySelectorAll('main section[id], main div[id="more"]').forEach((s) => spy.observe(s));
}
