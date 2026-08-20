// BoundaryLine — 1.5px dashed grey line with capsule label centred on top.
const BoundaryLine = ({ label }) => (
  <div className="pg-boundary">
    {label && <span className="pg-boundary-label">{label}</span>}
  </div>
);

window.BoundaryLine = BoundaryLine;
