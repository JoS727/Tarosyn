const menu = document.querySelector('.menu');
const nav = document.querySelector('.site-header nav');

document.getElementById('year').textContent = new Date().getFullYear();

menu.addEventListener('click', () => {
  const open = nav.classList.toggle('is-open');
  menu.setAttribute('aria-expanded', String(open));
  menu.querySelector('span').textContent = open ? '—' : '+';
});

nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
  nav.classList.remove('is-open');
  menu.setAttribute('aria-expanded', 'false');
  menu.querySelector('span').textContent = '+';
}));
