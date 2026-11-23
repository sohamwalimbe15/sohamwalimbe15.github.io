// Placeholder links (data-todo) should not jump to the top of the page.
document.querySelectorAll('a[data-todo]').forEach((a) => {
  a.title = 'Link not added yet';
  a.addEventListener('click', (e) => e.preventDefault());
});
