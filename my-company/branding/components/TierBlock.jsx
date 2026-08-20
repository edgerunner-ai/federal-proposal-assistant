// TierBlock — neutral or hero variant. Optional 4-column row of children.
const TierBlock = ({ name, sub, hero = false, columns = [] }) => (
  <div className={`pg-tier ${hero ? "pg-tier-hero" : "pg-tier-neutral"}`}>
    <div style={{ textAlign: "center" }}>
      <div className="pg-tier-name">{name}</div>
      {sub && <div className="pg-tier-sub">{sub}</div>}
    </div>
    {columns.length > 0 && (
      <div className="pg-tier-cols">
        {columns.map((c, i) => <div className="pg-tier-col" key={i}>{c}</div>)}
      </div>
    )}
  </div>
);

window.TierBlock = TierBlock;
