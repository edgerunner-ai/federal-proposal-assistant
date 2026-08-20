// RegistryPill — solid red uppercase pill (e.g. ENTERPRISE MODEL REGISTRY).
const RegistryPill = ({ children, style }) => (
  <div style={{ textAlign: "center", margin: "8px 0", ...style }}>
    <span className="pg-pill">{children}</span>
  </div>
);

window.RegistryPill = RegistryPill;
