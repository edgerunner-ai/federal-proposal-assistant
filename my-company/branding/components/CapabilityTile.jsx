// CapabilityTile — coloured-header tile used in SOF / IC / Acq / Service grids.
const TILE_COLORS = {
  red:   { border: "#ee2929", bg: "#ee2929", fg: "#191c20" },
  amber: { border: "#c8a200", bg: "#c8a200", fg: "#191c20" },
  blue:  { border: "#3d6fa3", bg: "#3d6fa3", fg: "#ffffff" },
  green: { border: "#5a7d5a", bg: "#5a7d5a", fg: "#ffffff" },
};

const CapabilityTile = ({ label, body, color = "red" }) => {
  const c = TILE_COLORS[color] || TILE_COLORS.red;
  return (
    <div className="pg-tile" style={{ borderColor: c.border }}>
      <div className="pg-tile-h" style={{ background: c.bg, color: c.fg }}>{label}</div>
      <div className="pg-tile-b">{body}</div>
    </div>
  );
};

window.CapabilityTile = CapabilityTile;
