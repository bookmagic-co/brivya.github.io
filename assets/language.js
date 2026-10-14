// 语言选择存储在浏览器中，不依赖 cookie 或第三方服务。
window.BrivyaSiteConfig = Object.freeze({ defaultLanguage: 'zh', supportedLanguages: ['zh', 'en'] });
document.querySelectorAll('[data-language]').forEach((link) => {
  link.addEventListener('click', () => {
    try { localStorage.setItem('brivya-language', link.dataset.language); } catch { /* 私密浏览仍可通过链接切换。 */ }
  });
});
// 只在首页复用主动选择；直接访问文档链接时尊重该链接的语言。
if (location.pathname === '/') {
  try {
    if (localStorage.getItem('brivya-language') === 'en') location.replace('/en/' + location.search + location.hash);
  } catch { /* 存储不可用时使用默认语言。 */ }
}
