window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
    skipHtmlTags: ["script", "noscript", "style", "textarea", "pre", "code"]
  }
};

// Если navigation.instant включён — используем document$
if (typeof document$ !== 'undefined') {
  document$.subscribe(() => {
    MathJax.startup.output.clearCache();
    MathJax.typesetClear();
    MathJax.texReset();
    MathJax.typesetPromise();
  });
} else {
  // Иначе ждём обычной загрузки страницы
  window.addEventListener('load', () => {
    MathJax.typesetPromise();
  });
}