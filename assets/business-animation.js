// 概念流程演示；不调用真实业务接口，不生成模拟交易结果。
(() => {
  const demo = document.querySelector('[data-business-demo]');
  if (!demo) return;
  const english = document.documentElement.lang === 'en';
  const scenes = english ? [
    ['Discover a capability', 'An AI host discovers menu.search and availability.check from a typed business contract. Discovery describes what exists; it does not grant permission.', 'Business value: expose capabilities once, across multiple entry points.'],
    ['Turn intent into a request', 'The host turns a reservation intent into structured business input. A trusted service supplies identity and delegation context.', 'Business value: move from conversation to a typed, verifiable request.'],
    ['Apply business controls', 'Validation, authorization, policy and approval when required govern execution. A client confirmation cannot replace trusted approval.', 'Business value: keep control of who can act, and under which conditions.'],
    ['Execute and leave evidence', 'The Connector executes the permitted action. Idempotency, transaction and audit evidence keep the business result traceable.', 'Business value: connect existing systems while preserving one execution truth.'],
  ] : [
    ['发现业务能力', 'AI 平台从类型化业务契约发现 menu.search 与 availability.check。发现说明能力存在，但不会授予执行权限。', '业务价值：一次定义能力，让多个入口理解你的业务。'],
    ['将意图变为请求', '平台将预订意图转为结构化业务输入。可信服务端提供身份与委托上下文。', '业务价值：从对话进入可验证、类型明确的业务请求。'],
    ['应用业务治理', '校验、授权、策略和必要的审批决定动作是否执行。客户端确认不能替代可信审批证据。', '业务价值：保留谁能执行、在什么条件下执行的控制权。'],
    ['执行并留下证据', 'Connector 执行被允许的动作，幂等、事务与审计让业务结果可追踪。', '业务价值：连接已有系统，同时保持一份执行真相。'],
  ];
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  const buttons = [...demo.querySelectorAll('[data-scene]')];
  const toggle = demo.querySelector('[data-demo-toggle]');
  let step = 0, timer = null, playing = false, visible = false, manual = null;
  function render() {
    demo.dataset.step = String(step);
    demo.querySelector('[data-demo-title]').textContent = scenes[step][0];
    demo.querySelector('[data-demo-description]').textContent = scenes[step][1];
    demo.querySelector('[data-demo-value]').textContent = scenes[step][2];
    demo.querySelector('[data-demo-counter]').textContent = `0${step + 1} / 04`;
    buttons.forEach((button, i) => {
      if (i === step) button.setAttribute('aria-current', 'step');
      else button.removeAttribute('aria-current');
    });
  }
  function run(value) {
    clearInterval(timer); timer = null; playing = value;
    demo.dataset.playing = String(value);
    toggle.textContent = english ? (value ? 'Pause animation' : 'Play animation') : (value ? '暂停动画' : '播放动画');
    toggle.setAttribute('aria-pressed', String(value));
    if (value) timer = setInterval(() => { step = (step + 1) % scenes.length; render(); }, 4500);
  }
  function sync() { run(visible && !document.hidden && (manual === null ? !motion.matches : manual)); }
  toggle.addEventListener('click', () => { manual = !playing; sync(); });
  buttons.forEach((button, i) => button.addEventListener('click', () => { step = i; manual = false; run(false); render(); }));
  motion.addEventListener('change', () => { manual = null; sync(); });
  document.addEventListener('visibilitychange', sync);
  if ('IntersectionObserver' in window) new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; sync(); }, { threshold: 0.2 }).observe(demo);
  else { visible = true; sync(); }
  render();
})();
