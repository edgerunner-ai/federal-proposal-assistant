// EdgeRunner AI — One-Slide Company Overview
// Builds a 13.33" × 7.5" widescreen PowerPoint slide that mirrors 07-company-overview.html
// Output: 07-company-overview.pptx in this same directory.

const path = require("path");

// Resolve global pptxgenjs install
let pptxgen;
try {
  pptxgen = require("pptxgenjs");
} catch (e) {
  const { execSync } = require("child_process");
  const globalRoot = execSync("npm root -g").toString().trim();
  pptxgen = require(path.join(globalRoot, "pptxgenjs"));
}

// ─── Color Palette (no "#" prefix per pptxgenjs requirement) ───
const C = {
  slideBg:    "14171B",
  panelBg:    "191D22",
  cardBg:     "1E2228",
  cardBg2:    "1A1E24",
  border:     "2A2D32",
  borderDim:  "25282D",
  red:        "C8102E",   // darker brand red — slide variant
  redBgSoft:  "2A0F14",   // approximate for rgba(200,16,46,.08) over dark
  redBgMed:   "3A1418",
  gold:       "C8A200",
  goldBg:     "2A2410",
  blue:       "5B9BD5",
  blueBg:     "162234",
  blueBg2:    "1A2940",
  blueBg3:    "1F3A55",
  green:      "64C878",
  greenBg:    "13261A",
  white:      "FFFFFF",
  textBright: "FFFFFF",
  textMid:    "D0D3D8",
  textBody:   "C8CDD4",
  textSub:    "9CA3AF",
  textMuted:  "8A8F96",
  textDim:    "6B7280",
  textVdim:   "4A5060",
};

const FONT = "Segoe UI";

// ─── Initialize Presentation ───
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33" × 7.5"
pres.author = "EdgeRunner AI";
pres.title  = "EdgeRunner AI — Company Overview";

const slide = pres.addSlide();
slide.background = { color: C.slideBg };

// ─── Helpers ───
function rect(opts) {
  slide.addShape(pres.shapes.RECTANGLE, opts);
}
function text(str, opts) {
  slide.addText(str, { fontFace: FONT, ...opts });
}
function richText(arr, opts) {
  slide.addText(arr, { fontFace: FONT, ...opts });
}
function line(x1, y1, x2, y2, color, width = 0.75) {
  slide.addShape(pres.shapes.LINE, {
    x: x1, y: y1, w: x2 - x1, h: y2 - y1,
    line: { color, width }
  });
}

// ============================================================
// HEADER (red bar) — y: 0 to 0.95
// ============================================================
rect({ x: 0, y: 0, w: 13.33, h: 0.95, fill: { color: C.red }, line: { color: C.red } });

// Logo image — placed on a white tile for contrast.
// Loads from my-company/branding/edgerunner-logo.png if present;
// otherwise falls back to text wordmark.
const fs = require("fs");
const logoPath = path.join(__dirname, "..", "branding", "edgerunner-logo.png");
if (fs.existsSync(logoPath)) {
  // Logo is the WhiteRed horizontal variant — "Edge" is white, "runner" is red.
  // Place directly on the red header bar; no backing tile (would hide "Edge").
  slide.addImage({ path: logoPath, x: 0.30, y: 0.18, w: 2.65, h: 0.55,
    sizing: { type: "contain", w: 2.65, h: 0.55 } });
} else {
  text([
    { text: "EdgeRunner ", options: { bold: true, color: C.white, fontSize: 24 } },
    { text: "AI",           options: { color: C.white, fontSize: 24, transparency: 15 } },
  ], { x: 0.30, y: 0.05, w: 3.0, h: 0.40, margin: 0, valign: "middle" });
}

text("Sovereign, On-Device AI for the Warfighter", {
  x: 0.30, y: 0.42, w: 3.0, h: 0.25, margin: 0,
  fontSize: 11, bold: true, color: C.white,
});

text("BELLEVUE, WA  ·  FOUNDED 2024  ·  WWW.EDGERUNNERAI.COM", {
  x: 0.30, y: 0.66, w: 3.0, h: 0.20, margin: 0,
  fontSize: 8, color: C.white, transparency: 30, charSpacing: 1,
});

// Vertical divider
line(3.30, 0.10, 3.30, 0.85, C.white, 1.5);

// Right side — value proposition
richText([
  { text: "A distributed tactical AI layer that runs ", options: { color: C.white, fontSize: 12 } },
  { text: "mission-tuned, open-weight models on-device",  options: { color: C.white, fontSize: 12, bold: true } },
  { text: " in disconnected, denied, intermittent & limited (DDIL) environments — and converts every operator interaction into ", options: { color: C.white, fontSize: 12 } },
  { text: "structured training data",                     options: { color: C.white, fontSize: 12, bold: true } },
  { text: " for continuous enterprise refinement.",       options: { color: C.white, fontSize: 12 } },
], { x: 3.45, y: 0.06, w: 9.70, h: 0.55, margin: 0, valign: "top" });

// Pillar pills row
const pillars = ["On-Device Execution", "Agentic Workflows", "Edge → Enterprise Data Loop"];
let pillX = 3.45;
const pillY = 0.65;
const pillH = 0.24;
pillars.forEach(p => {
  const w = 0.16 + p.length * 0.085; // approximate width fitting
  rect({ x: pillX, y: pillY, w, h: pillH,
    fill: { color: "000000", transparency: 82 },
    line: { color: C.white, width: 0.5, transparency: 75 }
  });
  text(p.toUpperCase(), {
    x: pillX, y: pillY, w, h: pillH, margin: 0,
    fontSize: 8, bold: true, color: C.white, align: "center", valign: "middle", charSpacing: 1,
  });
  pillX += w + 0.12;
});

// ============================================================
// BODY — y: 0.95 to 7.5
// Three columns: LEFT (3.10) | CENTER (7.10) | RIGHT (3.13)
// ============================================================

// ─── LEFT PANEL ───
const LX = 0, LW = 3.10, BY = 0.95, BH = 6.55;
rect({ x: LX, y: BY, w: LW, h: BH, fill: { color: C.panelBg }, line: { color: C.border } });

// Title: CORE CAPABILITIES
text("CORE CAPABILITIES", {
  x: LX + 0.20, y: BY + 0.14, w: LW - 0.40, h: 0.28, margin: 0,
  fontSize: 14, bold: true, color: C.red, charSpacing: 1.5,
});
line(LX + 0.20, BY + 0.46, LX + LW - 0.20, BY + 0.46, C.border, 0.5);

// Capabilities list
const caps = [
  ["On-Device Model Execution",   "Zero cloud dependency · runs in DDIL · 16GB VRAM commodity hardware"],
  ["On-Device Fine-Tuning",       "LoRA adapter specialization per MOS/AFSC without data leaving the edge"],
  ["Agentic Workflow Automation", "Multi-step task execution at point of mission · integrates into operator tools"],
  ["Operational Data Capture",    "Structured mission data → GCC for refinement · continuous feedback loop"],
  ["Standards-Based Inference",   "Drop-in API · servers, workstations, laptops, TAK, fly-away kits"],
];
let capY = BY + 0.55;
caps.forEach(([name, desc]) => {
  // dot
  slide.addShape(pres.shapes.OVAL, {
    x: LX + 0.22, y: capY + 0.07, w: 0.07, h: 0.07,
    fill: { color: C.red }, line: { color: C.red }
  });
  text(name, {
    x: LX + 0.36, y: capY, w: LW - 0.50, h: 0.20, margin: 0,
    fontSize: 10, bold: true, color: C.white,
  });
  text(desc, {
    x: LX + 0.36, y: capY + 0.20, w: LW - 0.50, h: 0.34, margin: 0,
    fontSize: 8, color: C.textMuted,
  });
  capY += 0.62;
});

// Divider
line(LX + 0.20, capY + 0.02, LX + LW - 0.20, capY + 0.02, C.border, 0.5);
capY += 0.10;

// Mission Adapters
text("MISSION ADAPTERS (LoRA)", {
  x: LX + 0.20, y: capY, w: LW - 0.40, h: 0.20, margin: 0,
  fontSize: 9, bold: true, color: C.gold, charSpacing: 1,
});
capY += 0.22;

const adapters = ["Logistics", "Combat Medic", "Combat Arms", "Maintenance", "Acquisitions", "Cyber", "SIGINT"];
let adX = LX + 0.20;
let adY = capY;
const adH = 0.22;
adapters.forEach(a => {
  const w = 0.18 + a.length * 0.072;
  if (adX + w > LX + LW - 0.20) { adX = LX + 0.20; adY += 0.27; }
  rect({ x: adX, y: adY, w, h: adH,
    fill: { color: C.goldBg }, line: { color: C.gold, width: 0.5 }
  });
  text(a, { x: adX, y: adY, w, h: adH, margin: 0,
    fontSize: 8, bold: true, color: C.gold, align: "center", valign: "middle" });
  adX += w + 0.06;
});
capY = adY + 0.36;

// Published Research callout
const prH = 1.15;
rect({ x: LX + 0.20, y: capY, w: LW - 0.40, h: prH,
  fill: { color: C.redBgSoft }, line: { color: C.red, width: 0.5 }
});
text("PUBLISHED RESEARCH", {
  x: LX + 0.30, y: capY + 0.08, w: LW - 0.60, h: 0.20, margin: 0,
  fontSize: 9, bold: true, color: C.red, charSpacing: 1,
});
richText([
  { text: "MilDeflect: ", options: { bold: true, color: C.white, fontSize: 9 } },
  { text: "Commercial LLMs refuse up to 98.2% of legitimate military tasks", options: { color: C.textMid, fontSize: 9 } },
], { x: LX + 0.30, y: capY + 0.30, w: LW - 0.60, h: 0.40, margin: 0 });
richText([
  { text: "EdgeRunner 20B: ", options: { bold: true, color: C.white, fontSize: 9 } },
  { text: "Matches / exceeds GPT-5 on military tasks on tactical hardware", options: { color: C.textMid, fontSize: 9 } },
], { x: LX + 0.30, y: capY + 0.70, w: LW - 0.60, h: 0.40, margin: 0 });


// ─── CENTER PANEL ───
const CX = 3.10, CW = 7.13;
// no panel background; transparent

text("TECHNICAL ARCHITECTURE", {
  x: CX + 0.25, y: BY + 0.14, w: CW - 0.50, h: 0.28, margin: 0,
  fontSize: 14, bold: true, color: C.blue, charSpacing: 1.5,
});
line(CX + 0.25, BY + 0.46, CX + CW - 0.25, BY + 0.46, C.border, 0.5);

// ── Stack diagram (bottom-up: silicon → app) — drawn top-down per HTML order ──
// Each row: label box (1.55") + content area (rest)
const stackX = CX + 0.25;
const stackW = CW - 0.50;
const labelW = 1.55;
const contentX = stackX + labelW + 0.08;
const contentW = stackW - labelW - 0.08;
const rowH = 0.36;
let stackY = BY + 0.58;

function stackRow(labelLines, contentParts, bg, borderColor, labelColor) {
  rect({ x: stackX, y: stackY, w: stackW, h: rowH,
    fill: { color: bg }, line: { color: borderColor, width: 0.5 }
  });
  // label
  text(labelLines.map(l => l.toUpperCase()).join("\n"), {
    x: stackX + 0.10, y: stackY, w: labelW, h: rowH, margin: 0,
    fontSize: 8, bold: true, color: labelColor, valign: "middle", charSpacing: 1,
  });
  // content
  if (typeof contentParts === "string") {
    text(contentParts, {
      x: contentX, y: stackY, w: contentW, h: rowH, margin: 0,
      fontSize: 9.5, color: C.textBody, valign: "middle",
    });
  } else {
    richText(contentParts, {
      x: contentX, y: stackY, w: contentW, h: rowH, margin: 0,
      fontSize: 9.5, valign: "middle",
    });
  }
  stackY += rowH + 0.05;
}

// Top row: Application
stackRow(
  ["Secure Application", "Runtime"],
  [
    { text: "EdgeRunner UI/UX  ·  ",                           options: { color: C.textBody, fontSize: 9.5 } },
    { text: "WarClaw",                                          options: { color: C.white, fontSize: 9.5, bold: true } },
    { text: " Agentic Layer  ·  Standards-Based Inference API  ·  DoD System Integrations", options: { color: C.textBody, fontSize: 9.5 } },
  ],
  C.redBgMed, C.red, C.red
);

// LoRAs
stackRow(
  ["Mission LoRAs"],
  "Logistics  ·  Combat Medicine  ·  Combat Arms  ·  Maintenance  ·  Acquisitions  ·  Cyber  ·  SIGINT",
  C.goldBg, C.gold, C.gold
);

// LLMs row with tier pills
rect({ x: stackX, y: stackY, w: stackW, h: rowH,
  fill: { color: C.blueBg }, line: { color: C.blue, width: 0.5 }
});
text("EDGERUNNER MILSPEC\n+ OTHER MODELS", {
  x: stackX + 0.10, y: stackY, w: labelW, h: rowH, margin: 0,
  fontSize: 8, bold: true, color: C.blue, valign: "middle", charSpacing: 1,
});
// Three tier pills inline
const tierLabels = [
  { label: "Light · ~4B",       bg: C.blueBg,  border: C.blue,   text: C.blue   },
  { label: "Medium · ~20–26B",  bg: C.blueBg2, border: C.blue,   text: "7AB3E0" },
  { label: "Heavy · ~70–120B",  bg: C.blueBg3, border: C.blue,   text: "A8CCF0" },
];
let tx = contentX;
const tierY = stackY + 0.07;
const tierH = 0.22;
tierLabels.forEach(t => {
  const w = 0.18 + t.label.length * 0.075;
  rect({ x: tx, y: tierY, w, h: tierH,
    fill: { color: t.bg }, line: { color: t.border, width: 0.5 }
  });
  text(t.label, { x: tx, y: tierY, w, h: tierH, margin: 0,
    fontSize: 8, bold: true, color: t.text, align: "center", valign: "middle" });
  tx += w + 0.08;
});
text("— no full retraining required · LoRA updates deployable in field", {
  x: tx + 0.05, y: stackY, w: contentX + contentW - tx - 0.05, h: rowH, margin: 0,
  fontSize: 8, color: C.textDim, valign: "middle",
});
stackY += rowH + 0.05;

// Inference Runtime
stackRow(
  ["Inference Runtime"],
  "ONNX  ·  CUDA  ·  Metal  ·  Vulkan  ·  OpenVINO",
  "1A1D22", C.border, C.textDim
);

// Silicon
stackRow(
  ["Silicon"],
  "AMD  ·  Intel  ·  NVIDIA  ·  Apple  ·  Qualcomm",
  "181B20", C.borderDim, C.textVdim
);

stackY += 0.05;

// ── Deployment Spectrum ──
const deployY = stackY;
const deployH = 0.62;
const deployCardW = (stackW - 0.16) / 3;
const deployCards = [
  { icon: "📱", name: "ATAK / Smartphone", spec: "6GB+ VRAM  ·  ~4B param  ·  Light" },
  { icon: "💻", name: "Laptop / Tablet",   spec: "16GB+ VRAM  ·  ~20–26B param  ·  Medium" },
  { icon: "🖥",  name: "On-Prem / VPC",     spec: "80GB+ VRAM  ·  ~70–120B param  ·  Heavy" },
];
deployCards.forEach((d, i) => {
  const dx = stackX + i * (deployCardW + 0.08);
  rect({ x: dx, y: deployY, w: deployCardW, h: deployH,
    fill: { color: C.cardBg2 }, line: { color: C.border, width: 0.5 }
  });
  text(d.icon, { x: dx, y: deployY + 0.04, w: deployCardW, h: 0.20, margin: 0,
    fontSize: 12, color: C.white, align: "center", valign: "middle" });
  text(d.name, { x: dx, y: deployY + 0.22, w: deployCardW, h: 0.20, margin: 0,
    fontSize: 10, bold: true, color: C.white, align: "center", valign: "middle" });
  text(d.spec, { x: dx, y: deployY + 0.40, w: deployCardW, h: 0.18, margin: 0,
    fontSize: 8, color: C.textMuted, align: "center", valign: "middle" });
});
stackY = deployY + deployH + 0.18;

// ── Teaming Partners ──
text("TEAMING PARTNERS — COHESIVE SOLUTION", {
  x: stackX, y: stackY, w: stackW, h: 0.22, margin: 0,
  fontSize: 11, bold: true, color: C.textSub, charSpacing: 1,
});
stackY += 0.26;

const partners = [
  { name: "System Integrators",   role: "Platform integration · classified deployment pathways",   badge: "SI LAYER",        color: C.blue },
  { name: "Analytics Providers",  role: "Enterprise analytics · decision support · GCC data exploitation",        badge: "ANALYTICS",       color: C.gold },
  { name: "AI Frontier Models",   role: "Foundation model providers · cloud AI complement · evaluation",          badge: "MODEL LAYER",     color: C.green },
  { name: "Commercial OEMs",      role: "HP · Panasonic (ruggedized hardware)  |  AMD · Intel (silicon)",         badge: "HARDWARE",        color: C.blue },
];
const partCardW = (stackW - 0.18) / 4;
const partH = 1.05;
partners.forEach((p, i) => {
  const px = stackX + i * (partCardW + 0.06);
  rect({ x: px, y: stackY, w: partCardW, h: partH,
    fill: { color: C.cardBg }, line: { color: C.border, width: 0.5 }
  });
  text(p.name, { x: px + 0.06, y: stackY + 0.06, w: partCardW - 0.12, h: 0.22, margin: 0,
    fontSize: 9.5, bold: true, color: C.white, align: "center" });
  text(p.role, { x: px + 0.06, y: stackY + 0.30, w: partCardW - 0.12, h: 0.50, margin: 0,
    fontSize: 7.5, color: C.textMuted, align: "center" });
  // badge
  const bw = 0.10 + p.badge.length * 0.06;
  const bx = px + (partCardW - bw) / 2;
  rect({ x: bx, y: stackY + partH - 0.26, w: bw, h: 0.20,
    fill: { color: "000000", transparency: 75 }, line: { color: p.color, width: 0.5 }
  });
  text(p.badge, { x: bx, y: stackY + partH - 0.26, w: bw, h: 0.20, margin: 0,
    fontSize: 7, bold: true, color: p.color, align: "center", valign: "middle", charSpacing: 0.8 });
});
stackY += partH + 0.18;

// ── Active R&D Partnerships ──
text("ACTIVE R&D PARTNERSHIPS", {
  x: stackX, y: stackY, w: stackW, h: 0.22, margin: 0,
  fontSize: 11, bold: true, color: C.textSub, charSpacing: 1,
});
stackY += 0.26;

const rdPartners = [
  { abbr: "AFRL", name: "Air Force Research Lab",   type: "CRADA" },
  { abbr: "ARL",  name: "Army Research Lab",        type: "CRADA + Joint Work Statement" },
  { abbr: "AI2C", name: "Army AI Integration Center", type: "Research Partnership" },
  { abbr: "NIWC", name: "NIWC Atlantic",            type: "Research Partnership" },
  { abbr: "USSF", name: "U.S. Space Force",         type: "On Contract" },
];
const rdCardW = (stackW - 0.24) / 5;
const rdH = 0.92;
rdPartners.forEach((r, i) => {
  const rx = stackX + i * (rdCardW + 0.06);
  rect({ x: rx, y: stackY, w: rdCardW, h: rdH,
    fill: { color: C.cardBg2 }, line: { color: C.border, width: 0.5 }
  });
  text(r.abbr, { x: rx, y: stackY + 0.04, w: rdCardW, h: 0.18, margin: 0,
    fontSize: 9, bold: true, color: C.blue, align: "center", charSpacing: 0.8 });
  text(r.name, { x: rx, y: stackY + 0.22, w: rdCardW, h: 0.36, margin: 0,
    fontSize: 8.5, bold: true, color: C.textMid, align: "center", valign: "top" });
  text(r.type, { x: rx, y: stackY + 0.56, w: rdCardW, h: 0.34, margin: 0,
    fontSize: 7.5, color: C.textDim, align: "center", valign: "top" });
});

// ─── RIGHT PANEL ───
const RX = 10.23, RW = 3.10;
rect({ x: RX, y: BY, w: RW, h: BH, fill: { color: C.panelBg }, line: { color: C.border } });

text("OPERATIONAL USERS", {
  x: RX + 0.20, y: BY + 0.14, w: RW - 0.40, h: 0.28, margin: 0,
  fontSize: 14, bold: true, color: C.red, charSpacing: 1.5,
});
line(RX + 0.20, BY + 0.46, RX + RW - 0.20, BY + 0.46, C.border, 0.5);

// User cards
const users = [
  { icon: "🎯", iconBg: C.redBgSoft, iconBorder: C.red,   name: "USASOC",            detail: "U.S. Army Special Operations Command", pill: { type: "trl", text: "Deployed · TRL 8" } },
  { icon: "⚔",  iconBg: C.goldBg,    iconBorder: C.gold,  name: "4th Infantry Division", detail: "U.S. Army · Conventional Forces",   pill: { type: "trl", text: "Deployed · TRL 8" } },
  { icon: "🛡", iconBg: C.greenBg,   iconBorder: C.green, name: "101st Infantry Brigade", detail: "U.S. Army · Conventional Forces",  pill: { type: "trl", text: "Deployed · TRL 8" } },
  { icon: "⚓", iconBg: C.blueBg,    iconBorder: C.blue,  name: "Navy ICOP",         detail: "Installations & Command Ops · PMW 120 / PEO C4I (NAVWAR)", pill: { type: "por", text: "PROGRAM OF RECORD · TRL 8" } },
];
let uY = BY + 0.55;
const uW = RW - 0.40;
users.forEach(u => {
  const isPOR = u.pill.type === "por";
  const cardH = isPOR ? 1.15 : 0.78;
  rect({ x: RX + 0.20, y: uY, w: uW, h: cardH,
    fill: { color: C.cardBg }, line: { color: C.border, width: 0.5 }
  });
  // icon box
  rect({ x: RX + 0.30, y: uY + 0.12, w: 0.36, h: 0.36,
    fill: { color: u.iconBg }, line: { color: u.iconBorder, width: 0.5 }
  });
  text(u.icon, { x: RX + 0.30, y: uY + 0.12, w: 0.36, h: 0.36, margin: 0,
    fontSize: 14, color: C.white, align: "center", valign: "middle" });
  // name
  text(u.name, { x: RX + 0.74, y: uY + 0.06, w: uW - 0.60, h: 0.22, margin: 0,
    fontSize: 10, bold: true, color: C.white });
  // detail
  text(u.detail, { x: RX + 0.74, y: uY + 0.26, w: uW - 0.60, h: isPOR ? 0.40 : 0.20, margin: 0,
    fontSize: 7.5, color: C.textMuted });
  // pill(s)
  if (isPOR) {
    rect({ x: RX + 0.74, y: uY + 0.78, w: 1.30, h: 0.20,
      fill: { color: C.redBgMed }, line: { color: C.red, width: 0.5 }
    });
    text("PROGRAM OF RECORD", { x: RX + 0.74, y: uY + 0.78, w: 1.30, h: 0.20, margin: 0,
      fontSize: 7, bold: true, color: C.red, align: "center", valign: "middle", charSpacing: 0.6 });
    rect({ x: RX + 2.08, y: uY + 0.78, w: 0.50, h: 0.20,
      fill: { color: C.greenBg }, line: { color: C.green, width: 0.5 }
    });
    text("TRL 8", { x: RX + 2.08, y: uY + 0.78, w: 0.50, h: 0.20, margin: 0,
      fontSize: 7, bold: true, color: C.green, align: "center", valign: "middle" });
  } else {
    rect({ x: RX + 0.74, y: uY + 0.50, w: 1.05, h: 0.20,
      fill: { color: C.greenBg }, line: { color: C.green, width: 0.5 }
    });
    text(u.pill.text, { x: RX + 0.74, y: uY + 0.50, w: 1.05, h: 0.20, margin: 0,
      fontSize: 7, bold: true, color: C.green, align: "center", valign: "middle" });
  }
  uY += cardH + 0.10;
});

// Investment block
const invH = 0.78;
rect({ x: RX + 0.20, y: uY, w: uW, h: invH,
  fill: { color: C.redBgSoft }, line: { color: C.red, width: 0.5 }
});
text("INVESTMENT RAISED", { x: RX + 0.30, y: uY + 0.06, w: uW - 0.20, h: 0.18, margin: 0,
  fontSize: 9, bold: true, color: C.red, charSpacing: 1 });
text("$17.5M", { x: RX + 0.30, y: uY + 0.22, w: uW - 0.20, h: 0.36, margin: 0,
  fontSize: 24, bold: true, color: C.white });
richText([
  { text: "Seed + Series A  ·  Led by ", options: { color: C.textBody, fontSize: 8 } },
  { text: "Madrona Ventures",            options: { color: C.white,    fontSize: 8, bold: true } },
], { x: RX + 0.30, y: uY + 0.58, w: uW - 0.20, h: 0.18, margin: 0 });
uY += invH + 0.12;

// Procurement & Credentials
const credH = 1.10;
rect({ x: RX + 0.20, y: uY, w: uW, h: credH,
  fill: { color: C.cardBg2 }, line: { color: C.border, width: 0.5 }
});
text("PROCUREMENT & CREDENTIALS", { x: RX + 0.30, y: uY + 0.06, w: uW - 0.20, h: 0.18, margin: 0,
  fontSize: 8, bold: true, color: C.textDim, charSpacing: 1 });

const creds = [
  ["CDAO Tradewinds", "Awardable ✓", true],
  ["CAGE",            "9Z176",       false],
  ["UEI",             "SLZTJUA8DBD3", false],
  ["NAICS",           "541511",      false],
];
let credY = uY + 0.28;
const credRowH = 0.18;
creds.forEach(([k, v, green], i) => {
  text(k, { x: RX + 0.30, y: credY, w: 1.30, h: credRowH, margin: 0,
    fontSize: 8.5, color: C.textMuted, valign: "middle" });
  text(v, { x: RX + 1.50, y: credY, w: uW - 1.40, h: credRowH, margin: 0,
    fontSize: 8.5, bold: true, color: green ? C.green : C.textMid,
    align: "right", valign: "middle" });
  if (i < creds.length - 1) {
    line(RX + 0.30, credY + credRowH, RX + RW - 0.30, credY + credRowH, "22262C", 0.4);
  }
  credY += credRowH + 0.02;
});

// ─── Write file ───
// Try the canonical path first; if locked (PowerPoint has it open),
// fall back to a v2 file so we don't crash.
function pickWritablePath(dir, base, ext) {
  const fs = require("fs");
  const primary = path.join(dir, `${base}${ext}`);
  try {
    if (!fs.existsSync(primary)) return primary;
    const fd = fs.openSync(primary, "r+");
    fs.closeSync(fd);
    return primary;
  } catch (e) {
    return path.join(dir, `${base}-v2${ext}`);
  }
}
const outPath = pickWritablePath(__dirname, "07-company-overview", ".pptx");
pres.writeFile({ fileName: outPath }).then(file => {
  console.log("Wrote:", file);
});
