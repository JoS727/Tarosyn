/* Google Analytics 4 for tarosyn.com.
   Same GA4 property/stream as tarosyn.app (G-BZFQJ5J4Y5) with cross-domain
   linking, so a visit that starts here and continues in the app is one journey.
   Consent Mode v2: analytics cookies are off by default in the EEA, UK and
   Switzerland (cookieless pings only) until a consent banner exists; ad
   storage is denied everywhere. */
(function () {
  var ID = 'G-BZFQJ5J4Y5';
  var CONSENT_REGIONS = ['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE','IS','LI','NO','GB','CH'];
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  var ads = { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' };
  gtag('consent', 'default', Object.assign({ analytics_storage: 'granted' }, ads));
  gtag('consent', 'default', Object.assign({ analytics_storage: 'denied', region: CONSENT_REGIONS }, ads));
  gtag('js', new Date());
  gtag('config', ID, { linker: { domains: ['tarosyn.com', 'tarosyn.app'] } });
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + ID;
  document.head.appendChild(s);
})();
