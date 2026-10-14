// 复制失败时明确提示，避免把权限拒绝误报为成功。
document.querySelectorAll('[data-copy]').forEach((button) => {
  const english = document.documentElement.lang === 'en';
  button.addEventListener('click', async () => {
    const code = document.getElementById(button.dataset.copy);
    const status = document.getElementById('copy-status');
    try {
      await navigator.clipboard.writeText(code.textContent.trim());
      button.textContent = english ? 'Copied' : '已复制';
      status.textContent = english ? 'Quick Start commands copied.' : 'Quick Start 命令已复制。';
    } catch {
      button.textContent = english ? 'Copy manually' : '请手动复制';
      status.textContent = english ? 'Clipboard unavailable. Select and copy the commands manually.' : '无法访问剪贴板，请选中命令手动复制。';
    }
    window.setTimeout(() => { button.textContent = english ? 'Copy' : '复制'; }, 2500);
  });
});
