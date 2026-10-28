import os

def create_header(filename, sys_code, title_en, title_jp, subtitle):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 72" width="100%" height="72">
  <defs>
    <!-- Bayer Matrix 1-Bit Dither Patterns (Strictly #050C2A & #E9EBFF) -->
    <pattern id="bayer12" width="8" height="8" patternUnits="userSpaceOnUse">
      <rect width="8" height="8" fill="#050C2A" />
      <rect x="0" y="0" width="2" height="2" fill="#E9EBFF" />
      <rect x="4" y="4" width="2" height="2" fill="#E9EBFF" />
    </pattern>
    <pattern id="bayer25" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="4" fill="#050C2A" />
      <rect x="0" y="0" width="2" height="2" fill="#E9EBFF" />
    </pattern>
    <pattern id="bayer50" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="4" fill="#050C2A" />
      <rect x="0" y="0" width="2" height="2" fill="#E9EBFF" />
      <rect x="2" y="2" width="2" height="2" fill="#E9EBFF" />
    </pattern>
    <pattern id="bayer75" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="4" fill="#E9EBFF" />
      <rect x="0" y="0" width="2" height="2" fill="#050C2A" />
    </pattern>
  </defs>

  <!-- Hard Offset Drop Shadow (4px 4px) -->
  <rect x="8" y="8" width="838" height="60" fill="#050C2A" shape-rendering="crispEdges"/>

  <!-- Main Chassis / Frame -->
  <rect x="4" y="4" width="838" height="60" fill="#050C2A" stroke="#E9EBFF" stroke-width="2" shape-rendering="crispEdges"/>

  <!-- Left Window Controls (PC-98 / Mac System 7 Style) -->
  <rect x="14" y="14" width="16" height="16" fill="#050C2A" stroke="#E9EBFF" stroke-width="2" shape-rendering="crispEdges"/>
  <rect x="18" y="21" width="8" height="2" fill="#E9EBFF" shape-rendering="crispEdges"/>

  <!-- Dither Spectrum Bar Left -->
  <rect x="38" y="14" width="10" height="40" fill="url(#bayer12)" shape-rendering="crispEdges" />
  <rect x="48" y="14" width="10" height="40" fill="url(#bayer25)" shape-rendering="crispEdges" />
  <rect x="58" y="14" width="10" height="40" fill="url(#bayer50)" shape-rendering="crispEdges" />
  <rect x="68" y="14" width="10" height="40" fill="url(#bayer75)" shape-rendering="crispEdges" />
  <rect x="78" y="14" width="6" height="40" fill="#E9EBFF" shape-rendering="crispEdges" />

  <!-- Title Badge -->
  <rect x="92" y="14" width="68" height="20" fill="#E9EBFF" shape-rendering="crispEdges"/>
  <text x="126" y="28" fill="#050C2A" font-family="'Courier New', monospace" font-size="11" font-weight="900" text-anchor="middle" letter-spacing="1">
    SYS::{sys_code}
  </text>

  <!-- Main Section Title -->
  <text x="168" y="30" fill="#E9EBFF" font-family="'Courier New', Courier, monospace" font-size="16" font-weight="900" letter-spacing="2">
    {title_en}
  </text>
  <text x="540" y="30" fill="#E9EBFF" font-family="'Courier New', 'MS Gothic', monospace" font-size="14" font-weight="bold" letter-spacing="3" opacity="0.9">
    // {title_jp}
  </text>

  <!-- Subtitle Terminal Prompt -->
  <text x="96" y="47" fill="#E9EBFF" font-family="'Courier New', monospace" font-size="10" letter-spacing="1" opacity="0.75">
    &gt;&gt; {subtitle}
  </text>

  <!-- System Telemetry Right -->
  <text x="715" y="26" fill="#E9EBFF" font-family="'Courier New', monospace" font-size="9" letter-spacing="1" opacity="0.8">
    [ROM: OK]
  </text>
  <text x="715" y="42" fill="#E9EBFF" font-family="'Courier New', monospace" font-size="9" letter-spacing="1" opacity="0.8">
    [CH: 1-BIT]
  </text>

  <!-- Dither Spectrum Bar Right -->
  <rect x="780" y="14" width="6" height="40" fill="#E9EBFF" shape-rendering="crispEdges" />
  <rect x="786" y="14" width="10" height="40" fill="url(#bayer75)" shape-rendering="crispEdges" />
  <rect x="796" y="14" width="10" height="40" fill="url(#bayer50)" shape-rendering="crispEdges" />
  <rect x="806" y="14" width="10" height="40" fill="url(#bayer25)" shape-rendering="crispEdges" />
  <rect x="816" y="14" width="10" height="40" fill="url(#bayer12)" shape-rendering="crispEdges" />

  <!-- Right Window Close Button -->
  <rect x="830" y="14" width="6" height="40" fill="#050C2A" stroke="#E9EBFF" stroke-width="1" shape-rendering="crispEdges"/>
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Updated {filename}")

def create_divider(filename):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 18" width="100%" height="18">
  <defs>
    <pattern id="div-dither25" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="4" fill="#050C2A" />
      <rect x="0" y="0" width="2" height="2" fill="#E9EBFF" />
    </pattern>
    <pattern id="div-dither50" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="4" fill="#050C2A" />
      <rect x="0" y="0" width="2" height="2" fill="#E9EBFF" />
      <rect x="2" y="2" width="2" height="2" fill="#E9EBFF" />
    </pattern>
    <pattern id="div-dither75" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="4" fill="#E9EBFF" />
      <rect x="0" y="0" width="2" height="2" fill="#050C2A" />
    </pattern>
  </defs>

  <rect x="0" y="8" width="220" height="2" fill="#E9EBFF" shape-rendering="crispEdges"/>
  <rect x="220" y="7" width="40" height="4" fill="url(#div-dither25)" shape-rendering="crispEdges"/>
  <rect x="260" y="6" width="40" height="6" fill="url(#div-dither50)" shape-rendering="crispEdges"/>
  <rect x="300" y="5" width="40" height="8" fill="url(#div-dither75)" shape-rendering="crispEdges"/>
  
  <!-- Center Plate -->
  <rect x="340" y="3" width="170" height="12" fill="#050C2A" stroke="#E9EBFF" stroke-width="1.5" shape-rendering="crispEdges"/>
  <text x="425" y="12" fill="#E9EBFF" font-family="'Courier New', monospace" font-size="9" font-weight="900" text-anchor="middle" letter-spacing="2">
    ░▒▓ PC-9801 ▓▒░
  </text>

  <rect x="510" y="5" width="40" height="8" fill="url(#div-dither75)" shape-rendering="crispEdges"/>
  <rect x="550" y="6" width="40" height="6" fill="url(#div-dither50)" shape-rendering="crispEdges"/>
  <rect x="590" y="7" width="40" height="4" fill="url(#div-dither25)" shape-rendering="crispEdges"/>
  <rect x="630" y="8" width="220" height="2" fill="#E9EBFF" shape-rendering="crispEdges"/>
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Updated {filename}")

def create_sys_bar(filename):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 36" width="100%" height="36">
  <defs>
    <pattern id="sys-dither50" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="4" fill="#050C2A" />
      <rect x="0" y="0" width="2" height="2" fill="#E9EBFF" />
      <rect x="2" y="2" width="2" height="2" fill="#E9EBFF" />
    </pattern>
  </defs>

  <rect x="4" y="4" width="842" height="28" fill="#050C2A" stroke="#E9EBFF" stroke-width="1.5" shape-rendering="crispEdges"/>
  
  <rect x="8" y="8" width="20" height="20" fill="url(#sys-dither50)" shape-rendering="crispEdges" />
  <rect x="14" y="14" width="8" height="8" fill="#050C2A" stroke="#E9EBFF" stroke-width="1" shape-rendering="crispEdges" />

  <text x="36" y="22" fill="#E9EBFF" font-family="'Courier New', monospace" font-size="11" font-weight="bold" letter-spacing="2">
    BIOS V98.01 // SYSTEM: TANVIR_MAIN // ARCHITECTURE: 64-BIT FULL-STACK // STATUS: [ONLINE]
  </text>

  <rect x="822" y="8" width="20" height="20" fill="url(#sys-dither50)" shape-rendering="crispEdges" />
  <rect x="828" y="14" width="8" height="8" fill="#050C2A" stroke="#E9EBFF" stroke-width="1" shape-rendering="crispEdges" />
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Updated {filename}")

os.makedirs("assets", exist_ok=True)
create_header("assets/header-about.svg", "01", "ABOUT_ME", "概要録", "OPERATOR IDENTITY // BIOGRAPHY // ACADEMIC DOSSIER")
create_header("assets/header-tech.svg", "02", "SYSTEM_SPECIFICATIONS", "技術仕様", "RUNTIME ENVIRONMENTS // LANGUAGES // ARCHITECTURES")
create_header("assets/header-projects.svg", "03", "MISSION_REPOSITORIES", "開発実績", "SOFTWARE SYSTEMS // CODEBASES // LABS")
create_header("assets/header-stats.svg", "04", "TELEMETRY_DIAGNOSTICS", "活動統計", "CONTRIBUTION RADAR // ACTIVITY STREAM // STREAK")
create_header("assets/header-contact.svg", "05", "COMMUNICATION_CHANNELS", "通信交信", "FREQUENCY RELAYS // DIRECT TRANSMISSION NODES")
create_divider("assets/divider.svg")
create_sys_bar("assets/sys-bar.svg")
