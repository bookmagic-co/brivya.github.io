// 复制失败时明确提示，避免把权限拒绝误报为成功。
document.querySelectorAll('[data-copy]').forEach((button) => {
  button.addEventListener('click', async () => {
    const code = document.getElementById(button.dataset.copy);
    const status = document.getElementById('copy-status');
    try {
      await navigator.clipboard.writeText(code.textContent.trim());
      button.textContent = '已复制';
      status.textContent = 'Quick Start 命令已复制。';
    } catch {
      button.textContent = '请手动复制';
      status.textContent = '无法访问剪贴板，请选中命令手动复制。';
    }
    window.setTimeout(() => { button.textContent = '复制'; }, 2500);
  });
});
