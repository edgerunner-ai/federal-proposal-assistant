// Canvas — outer 1200px frame with title bar and red rule.
const Canvas = ({ title, subtitle, children }) => (
  <div className="pg-canvas pg">
    {(title || subtitle) && (
      <div className="pg-canvas-title">
        {title && <h1>{title}</h1>}
        {subtitle && <p>{subtitle}</p>}
      </div>
    )}
    <div className="pg-canvas-body">{children}</div>
  </div>
);

window.Canvas = Canvas;
