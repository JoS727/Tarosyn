document.documentElement.classList.add('js');

const body = document.body;
const header = document.querySelector('[data-header]');
const navToggle = document.querySelector('.nav-toggle');
const nav = document.getElementById('primary-nav');
const year = document.getElementById('year');

if (year) year.textContent = new Date().getFullYear();

const syncHeader = () => {
  header?.classList.toggle('is-scrolled', window.scrollY > 18);
};

syncHeader();
window.addEventListener('scroll', syncHeader, { passive: true });

const closeNavigation = () => {
  body.classList.remove('nav-open');
  navToggle?.setAttribute('aria-expanded', 'false');
};

navToggle?.addEventListener('click', () => {
  const willOpen = !body.classList.contains('nav-open');
  body.classList.toggle('nav-open', willOpen);
  navToggle.setAttribute('aria-expanded', String(willOpen));
});

nav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeNavigation));

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') closeNavigation();
});

const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const reveals = document.querySelectorAll('.reveal');

if (reducedMotion || !('IntersectionObserver' in window)) {
  reveals.forEach((element) => element.classList.add('is-visible'));
} else {
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

  reveals.forEach((element) => revealObserver.observe(element));
}

document.querySelectorAll('.faq-list details').forEach((item) => {
  item.addEventListener('toggle', () => {
    if (!item.open) return;
    document.querySelectorAll('.faq-list details[open]').forEach((openItem) => {
      if (openItem !== item) openItem.removeAttribute('open');
    });
  });
});

document.querySelectorAll('[data-cta]').forEach((cta) => {
  cta.addEventListener('click', () => {
    const detail = { position: cta.dataset.cta, destination: cta.href };
    window.dispatchEvent(new CustomEvent('tarosyn:cta', { detail }));
    window.dataLayer?.push({ event: 'cta_click', cta_position: detail.position });
  });
});
