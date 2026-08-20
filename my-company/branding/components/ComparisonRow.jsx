// ComparisonRow — single row in the 3-state differentiator matrix.
// state values: "no" | "partial" | "yes"
const GLYPHS = { no: "✕", partial: "◐", yes: "●" };
const CLASSES = { no: "pg-cell-no", partial: "pg-cell-pa", yes: "pg-cell-yes" };

const ComparisonRow = ({ feature, columns }) => (
  <div className="pg-compare">
    <div className="pg-compare-label">{feature}</div>
    {columns.map((col, i) => (
      <div className={`pg-cell ${CLASSES[col.state]}`} key={i}>
        <span className="glyph">{GLYPHS[col.state]}</span>
        {col.text}
      </div>
    ))}
  </div>
);

const ComparisonHeader = ({ left = "Capability", columns }) => (
  <div className="pg-compare" style={{ borderBottom: "1.5px solid var(--pg-red)" }}>
    <div className="pg-compare-label" style={{ fontWeight: 700, color: "#fff", textTransform: "uppercase", letterSpacing: ".5px", fontSize: 13 }}>{left}</div>
    {columns.map((c, i) => (
      <div className="pg-cell" key={i} style={{ fontWeight: 700, color: "#fff", textTransform: "uppercase", letterSpacing: ".5px", fontSize: 13, background: "transparent" }}>
        {c}
      </div>
    ))}
  </div>
);

window.ComparisonRow = ComparisonRow;
window.ComparisonHeader = ComparisonHeader;
