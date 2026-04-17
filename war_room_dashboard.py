"""
╔══════════════════════════════════════════════════════════════════════╗
║   SALES COMMAND CENTER — LIVE REVENUE PULSE  WAR ROOM DASHBOARD     ║
║   Run:  streamlit run war_room_dashboard.py                          ║
║   Deps: pip install streamlit pandas plotly requests                 ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random
import time
import datetime
import requests

# ══════════════════════════════════════════════
#  PAGE CONFIG
# ══════════════════════════════════════════════
st.set_page_config(
    page_title="Sales Command Center — Live Revenue Pulse",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════
#  DESIGN SYSTEM — WARM GOLD × DEEP NAVY × CRIMSON
# ══════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;700&family=JetBrains+Mono:wght@400;700&display=swap');

:root {
    --navy:    #060d1a;
    --navy2:   #0b1628;
    --navy3:   #0f1e35;
    --card:    #111d30;
    --gold:    #f5c842;
    --gold2:   #e8a800;
    --crimson: #e8304a;
    --mint:    #2ecc9a;
    --sky:     #38b6f5;
    --purple:  #9b6dff;
    --text:    #e8edf5;
    --sub:     #8899b5;
    --border:  #1a2d4a;
    --rain:    #38b6f5;
    --heat:    #ff6b35;
    --font-title: 'Bebas Neue', sans-serif;
    --font-body:  'DM Sans', sans-serif;
    --font-mono:  'JetBrains Mono', monospace;
}

*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"], .stApp {
    background: var(--navy) !important;
    color: var(--text) !important;
    font-family: var(--font-body) !important;
}

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--navy2); }
::-webkit-scrollbar-thumb { background: var(--gold2); border-radius: 2px; }

#MainMenu, footer, header[data-testid="stHeader"] { display: none !important; }
.block-container { padding: 1.5rem 2rem !important; max-width: 100% !important; }

/* ── HERO ── */
.hero {
    background: linear-gradient(135deg, #0b1628 0%, #0f1e35 50%, #111530 100%);
    border: 1px solid var(--border);
    border-bottom: 3px solid var(--gold);
    border-radius: 10px;
    padding: 1.6rem 2.2rem;
    margin-bottom: 1.2rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 400px; height: 100%;
    background: radial-gradient(ellipse at right center, rgba(245,200,66,0.08) 0%, transparent 70%);
    pointer-events: none;
}
.hero-eyebrow {
    font-family: var(--font-mono);
    font-size: 0.68rem;
    color: var(--gold);
    letter-spacing: 0.35em;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
}
.hero-title {
    font-family: var(--font-title);
    font-size: 3.2rem;
    color: #ffffff;
    letter-spacing: 0.06em;
    line-height: 1;
    margin-bottom: 0.5rem;
}
.hero-title span { color: var(--gold); }
.hero-meta {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    color: var(--sub);
    letter-spacing: 0.15em;
    display: flex;
    align-items: center;
    gap: 1.2rem;
    flex-wrap: wrap;
}
.live-dot {
    display: inline-block;
    width: 7px; height: 7px;
    background: var(--mint);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--mint);
    animation: pulse-dot 1.4s ease-in-out infinite;
    margin-right: 5px;
}
@keyframes pulse-dot {
    0%, 100% { transform: scale(1); opacity: 1; }
    50%       { transform: scale(1.5); opacity: 0.5; }
}
.hero-badge {
    background: rgba(245,200,66,0.12);
    border: 1px solid rgba(245,200,66,0.3);
    border-radius: 20px;
    padding: 0.2rem 0.7rem;
    font-size: 0.6rem;
    color: var(--gold);
}

/* ── SECTION LABEL ── */
.sec-label {
    font-family: var(--font-mono);
    font-size: 0.62rem;
    font-weight: 700;
    color: var(--sub);
    letter-spacing: 0.35em;
    text-transform: uppercase;
    border-left: 3px solid var(--gold);
    padding-left: 0.7rem;
    margin: 1.4rem 0 0.8rem;
}

/* ── KPI CARDS ── */
.kpi {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1.2rem 1.4rem;
    position: relative;
    overflow: hidden;
    height: 100%;
}
.kpi::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
}
.kpi.gold::after   { background: var(--gold); }
.kpi.mint::after   { background: var(--mint); }
.kpi.sky::after    { background: var(--sky); }
.kpi.crimson::after{ background: var(--crimson); }
.kpi.purple::after { background: var(--purple); }
.kpi-icon  { font-size: 1.4rem; margin-bottom: 0.5rem; display: block; }
.kpi-label {
    font-family: var(--font-mono);
    font-size: 0.58rem;
    color: var(--sub);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 0.35rem;
}
.kpi-value {
    font-family: var(--font-title);
    font-size: 2rem;
    letter-spacing: 0.04em;
    line-height: 1;
    margin-bottom: 0.25rem;
}
.kpi-value.gold   { color: var(--gold); }
.kpi-value.mint   { color: var(--mint); }
.kpi-value.sky    { color: var(--sky); }
.kpi-value.crimson{ color: var(--crimson); }
.kpi-value.purple { color: var(--purple); }
.kpi-sub {
    font-family: var(--font-mono);
    font-size: 0.58rem;
    color: var(--sub);
}

/* ── WEATHER SECTION ── */
.weather-section {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.3rem 1.6rem;
    margin-bottom: 0.8rem;
}
.weather-section-title {
    font-family: var(--font-title);
    font-size: 1.5rem;
    color: white;
    letter-spacing: 0.08em;
    margin-bottom: 0.15rem;
}
.weather-section-sub {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    color: var(--sub);
    letter-spacing: 0.2em;
    margin-bottom: 1rem;
}
.weather-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 0.7rem;
}
.w-card {
    border-radius: 8px;
    padding: 0.9rem 0.8rem;
    text-align: center;
}
.w-card.rain {
    background: linear-gradient(160deg,#0a1e35,#0d2a4a);
    border: 1px solid #1a5080;
    border-top: 3px solid var(--rain);
}
.w-card.heat {
    background: linear-gradient(160deg,#2a0d08,#3a1205);
    border: 1px solid #7a2a10;
    border-top: 3px solid var(--heat);
}
.w-card.clear {
    background: linear-gradient(160deg,#0d2218,#0f2a1e);
    border: 1px solid #1a5535;
    border-top: 3px solid var(--mint);
}
.w-card.cloud {
    background: linear-gradient(160deg,#141e2a,#1a2535);
    border: 1px solid #2a3545;
    border-top: 3px solid #6688aa;
}
.w-card-city {
    font-family: var(--font-title);
    font-size: 1.05rem;
    letter-spacing: 0.1em;
    color: white;
    margin-bottom: 0.15rem;
}
.w-card-emoji { font-size: 1.8rem; margin-bottom: 0.3rem; display: block; }
.w-card-temp {
    font-family: var(--font-title);
    font-size: 1.6rem;
    letter-spacing: 0.05em;
    line-height: 1;
    margin-bottom: 0.15rem;
}
.w-card-temp.rain  { color: var(--rain); }
.w-card-temp.heat  { color: var(--heat); }
.w-card-temp.clear { color: var(--mint); }
.w-card-temp.cloud { color: #aabbcc; }
.w-card-desc {
    font-family: var(--font-mono);
    font-size: 0.58rem;
    color: var(--sub);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.w-card-stats {
    font-family: var(--font-mono);
    font-size: 0.54rem;
    color: var(--sub);
    display: flex;
    justify-content: center;
    gap: 0.4rem;
    margin-bottom: 0.5rem;
}
.w-impact {
    display: inline-block;
    border-radius: 20px;
    padding: 0.18rem 0.55rem;
    font-family: var(--font-mono);
    font-size: 0.55rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.w-impact.surge     { background:rgba(56,182,245,0.15); border:1px solid rgba(56,182,245,0.4); color:var(--rain); }
.w-impact.heat-warn { background:rgba(255,107,53,0.15); border:1px solid rgba(255,107,53,0.4); color:var(--heat); }
.w-impact.nominal   { background:rgba(46,204,154,0.12); border:1px solid rgba(46,204,154,0.3); color:var(--mint); }
.w-impact.moderate  { background:rgba(245,200,66,0.12); border:1px solid rgba(245,200,66,0.3); color:var(--gold); }

/* ── ALERTS ── */
.alert-strip {
    display: flex;
    align-items: center;
    gap: 1rem;
    background: linear-gradient(90deg,rgba(232,48,74,0.12),rgba(232,48,74,0.04));
    border: 1px solid rgba(232,48,74,0.4);
    border-left: 5px solid var(--crimson);
    border-radius: 6px;
    padding: 0.7rem 1.2rem;
    margin: 0.4rem 0;
    font-family: var(--font-mono);
    font-size: 0.72rem;
    color: #ff7090;
    animation: alert-pulse 2.5s ease-in-out infinite;
}
.alert-strip-rain {
    background: linear-gradient(90deg,rgba(56,182,245,0.12),rgba(56,182,245,0.04));
    border: 1px solid rgba(56,182,245,0.35);
    border-left: 5px solid var(--rain);
    color: #80ccff;
    animation: none;
}
@keyframes alert-pulse {
    0%,100% { border-left-color: var(--crimson); }
    50%      { border-left-color: rgba(232,48,74,0.15); }
}
.alert-badge {
    background: var(--crimson);
    color: white;
    border-radius: 4px;
    padding: 0.1rem 0.5rem;
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    white-space: nowrap;
}
.alert-badge.rain-badge { background: var(--rain); color: #060d1a; }

/* ── TICKER ── */
.ticker-outer {
    background: var(--navy2);
    border-top: 2px solid var(--gold2);
    border-bottom: 1px solid var(--border);
    padding: 0.45rem 0;
    overflow: hidden;
    white-space: nowrap;
    border-radius: 6px;
    margin-bottom: 0.8rem;
}
.ticker-inner { display:inline-block; animation:scroll-ticker 45s linear infinite; }
@keyframes scroll-ticker {
    0%   { transform: translateX(60vw); }
    100% { transform: translateX(-100%); }
}
.ticker-item {
    font-family: var(--font-mono);
    font-size: 0.68rem;
    color: var(--gold);
    letter-spacing: 0.05em;
    display: inline-block;
    padding: 0 2rem;
}
.t-city  { color: var(--sky); }
.t-price { color: var(--mint); font-weight: 700; }

/* ── FOOTER ── */
.dash-footer {
    font-family: var(--font-mono);
    font-size: 0.58rem;
    color: var(--sub);
    text-align: center;
    padding: 1rem 0 0.4rem;
    letter-spacing: 0.18em;
    border-top: 1px solid var(--border);
    margin-top: 1rem;
    opacity: 0.7;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  CONSTANTS
# ══════════════════════════════════════════════
WEATHER_API_KEY = "37b1806d95a16313402bc8a89f54a3a6"

PRODUCTS = [
    ("Enterprise Suite",   4999),
    ("Pro License",        1299),
    ("Starter Pack",        299),
    ("Analytics Add-on",    599),
    ("Support Contract",    899),
    ("Cloud Storage 1TB",   199),
    ("API Access",          749),
    ("Mobile SDK",          449),
    ("Data Pipeline",      2199),
    ("Security Module",    1499),
]

CITIES = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai",
    "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Surat",
]

CHART_COLORS = [
    "#f5c842","#2ecc9a","#38b6f5","#9b6dff","#e8304a",
    "#ff6b35","#44d4cc","#ffaa00","#ff88cc","#88ff66",
]

BASE_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(11,22,40,0.6)",
    font=dict(family="JetBrains Mono, monospace", color="#8899b5", size=10),
    margin=dict(l=10, r=10, t=36, b=10),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#8899b5", size=9)),
    xaxis=dict(gridcolor="rgba(26,45,74,0.7)", zerolinecolor="rgba(26,45,74,0.7)"),
    yaxis=dict(gridcolor="rgba(26,45,74,0.7)", zerolinecolor="rgba(26,45,74,0.7)"),
)


# ══════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════
def generate_sale():
    product, base = random.choice(PRODUCTS)
    return {
        "timestamp": datetime.datetime.now(),
        "time":      datetime.datetime.now().strftime("%H:%M:%S"),
        "product":   product,
        "price":     max(99, base + random.randint(-80, 300)),
        "city":      random.choice(CITIES),
    }


def get_weather(city: str) -> dict:
    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city},IN&appid={WEATHER_API_KEY}&units=metric"
        )
        r = requests.get(url, timeout=6)
        if r.status_code == 200:
            d = r.json()
            return {
                "desc":     d["weather"][0]["main"],
                "detail":   d["weather"][0]["description"].title(),
                "temp":     round(d["main"]["temp"], 1),
                "feels":    round(d["main"]["feels_like"], 1),
                "humidity": d["main"]["humidity"],
                "wind":     round(d["wind"]["speed"], 1),
                "source":   "live",
            }
    except Exception:
        pass
    # Simulated fallback
    options = [("Rain",25),("Clear",39),("Clouds",31),("Haze",35),("Thunderstorm",24)]
    desc, temp = random.choice(options)
    return {
        "desc": desc, "detail": desc,
        "temp": temp + random.randint(-2,2),
        "feels": temp + random.randint(-3,2),
        "humidity": random.randint(40,90),
        "wind": round(random.uniform(2,18),1),
        "source": "sim",
    }


def classify(desc: str, temp: float) -> str:
    d = desc.lower()
    if any(x in d for x in ("thunder","rain","drizzle")): return "rain"
    if temp >= 37: return "heat"
    if any(x in d for x in ("cloud","haze","fog","mist")): return "cloud"
    return "clear"


def w_emoji(cls: str) -> str:
    return {"rain":"🌧️","heat":"🔥","cloud":"☁️","clear":"☀️"}.get(cls,"🌤️")


def w_impact(cls: str, temp: float):
    if cls == "rain":   return "📈 ONLINE SURGE",    "surge",     "Rain boosts e-commerce"
    if cls == "heat":   return "⚠️ HEAT ALERT",      "heat-warn", "Foot traffic drops at 37°C+"
    if temp > 32:       return "📊 WARM/MODERATE",   "moderate",  "Slight indoor slowdown"
    return               "✅ NOMINAL",               "nominal",   "Conditions optimal"


# ══════════════════════════════════════════════
#  SESSION STATE
# ══════════════════════════════════════════════
if "sales" not in st.session_state:
    st.session_state.sales       = [generate_sale() for _ in range(15)]
    st.session_state.last_sale   = time.time() - 35
    st.session_state.weather     = {}
    st.session_state.weather_ts  = 0

now_ts = time.time()

if now_ts - st.session_state.last_sale >= 30:
    st.session_state.sales.append(generate_sale())
    st.session_state.last_sale = now_ts

st.session_state.sales = st.session_state.sales[-60:]

if now_ts - st.session_state.weather_ts > 300:
    for city in CITIES:
        st.session_state.weather[city] = get_weather(city)
    st.session_state.weather_ts = now_ts

# ── Derived ──────────────────────────────────
df         = pd.DataFrame(st.session_state.sales)
wc         = st.session_state.weather
total_rev  = int(df["price"].sum())
order_vol  = len(df)
avg_order  = int(df["price"].mean())
last5_rev  = int(df.tail(5)["price"].sum())
secs_next  = max(0, 30 - int(now_ts - st.session_state.last_sale))
city_rev   = df.groupby("city")["price"].sum().sort_values(ascending=False)
prod_rev   = df.groupby("product")["price"].sum().sort_values(ascending=False)
now_dt     = datetime.datetime.now()
is_live    = any(v.get("source") == "live" for v in wc.values())
w_src_tag  = "🛰 LIVE" if is_live else "◌ SIMULATED"


# ══════════════════════════════════════════════
#  ── HERO ──────────────────────────────────────
# ══════════════════════════════════════════════
st.markdown(f"""
<div class="hero">
  <div class="hero-eyebrow">🎯 Sales Command Center &nbsp;·&nbsp; Revenue Pulse &nbsp;·&nbsp; War Room Operations</div>
  <div class="hero-title">LIVE <span>REVENUE</span> DASHBOARD</div>
  <div class="hero-meta">
    <span><span class="live-dot"></span>LIVE STREAM ACTIVE</span>
    <span>📅 {now_dt.strftime('%A, %d %B %Y')}</span>
    <span>🕐 {now_dt.strftime('%H:%M:%S')}</span>
    <span class="hero-badge">WEATHER: {w_src_tag}</span>
    <span class="hero-badge">AUTO-REFRESH 5s</span>
    <span class="hero-badge">NEXT SALE: {secs_next}s</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── TICKER ─────────────────────────────────────
ticker = "".join([
    f'<span class="ticker-item">⚡ {s["product"]} '
    f'<span class="t-price">₹{s["price"]:,}</span> — '
    f'<span class="t-city">{s["city"]}</span> {s["time"]}</span>'
    for s in st.session_state.sales[-12:]
])
st.markdown(
    f'<div class="ticker-outer"><div class="ticker-inner">{ticker}</div></div>',
    unsafe_allow_html=True,
)

# ── KPI CARDS ──────────────────────────────────
st.markdown('<div class="sec-label">📊 COMMAND METRICS — REAL-TIME COUNTERS</div>', unsafe_allow_html=True)
k1, k2, k3, k4, k5 = st.columns(5)

def kpi(col, icon, label, val, sub, color):
    col.markdown(f"""
    <div class="kpi {color}">
      <span class="kpi-icon">{icon}</span>
      <div class="kpi-label">{label}</div>
      <div class="kpi-value {color}">{val}</div>
      <div class="kpi-sub">{sub}</div>
    </div>""", unsafe_allow_html=True)

kpi(k1, "💰", "Total Revenue",   f"₹{total_rev:,}", "Session cumulative",      "gold")
kpi(k2, "📦", "Order Volume",    str(order_vol),     "Last 60 orders",          "mint")
kpi(k3, "📈", "Avg Order Value", f"₹{avg_order:,}", "Rolling mean",            "sky")
kpi(k4, "⚡", "Last 5 Orders",   f"₹{last5_rev:,}", "Recent sprint total",     "purple")
kpi(k5, "⏱",  "Next Sale In",   f"{secs_next}s",    "Auto-generated feed",     "crimson")


# ══════════════════════════════════════════════
#  WEATHER INTELLIGENCE PANEL
# ══════════════════════════════════════════════
st.markdown('<div class="sec-label">🌦️ WEATHER INTELLIGENCE — LIVE CITY IMPACT ANALYSIS</div>',
            unsafe_allow_html=True)

wcards_html = ""
rain_cities, heat_cities = [], []

for city in CITIES:
    w      = wc.get(city, {"desc":"Clear","temp":30,"humidity":60,"wind":5,"source":"sim","detail":"Clear"})
    desc   = w.get("desc","Clear")
    temp   = w.get("temp", 30)
    hum    = w.get("humidity", 60)
    wind   = w.get("wind", 5)
    detail = w.get("detail", desc)
    cls    = classify(desc, temp)
    emo    = w_emoji(cls)
    imp_label, imp_cls, imp_desc = w_impact(cls, temp)

    if cls == "rain":  rain_cities.append(city)
    elif cls == "heat": heat_cities.append(city)

    wcards_html += f"""
    <div class="w-card {cls}">
      <span class="w-card-emoji">{emo}</span>
      <div class="w-card-city">{city}</div>
      <div class="w-card-temp {cls}">{temp}°C</div>
      <div class="w-card-desc">{detail}</div>
      <div class="w-card-stats"><span>💧{hum}%</span><span>💨{wind}m/s</span></div>
      <span class="w-impact {imp_cls}">{imp_label}</span>
    </div>"""

st.markdown(f"""
<div class="weather-section">
  <div class="weather-section-title">🌦️ Real-Time Weather × Sales Impact</div>
  <div class="weather-section-sub">OPENWEATHERMAP API · 10 MAJOR INDIAN CITIES · REFRESH EVERY 5 MIN</div>
  <div class="weather-grid">{wcards_html}</div>
</div>
""", unsafe_allow_html=True)

# ── ALERTS ─────────────────────────────────────
if rain_cities:
    st.markdown(f"""
    <div class="alert-strip alert-strip-rain">
      <span class="alert-badge rain-badge">🌧️ RAIN ALERT</span>
      <strong>Online sales surge expected</strong> in: {" · ".join(rain_cities)}
      — Rain drives customers to e-commerce. Push digital campaigns NOW.
    </div>""", unsafe_allow_html=True)

if heat_cities:
    st.markdown(f"""
    <div class="alert-strip">
      <span class="alert-badge">🔥 HEAT WARNING</span>
      <strong>Foot traffic drop risk</strong> in: {" · ".join(heat_cities)}
      — Above 37°C. Redirect to delivery &amp; online channels immediately.
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  CHARTS ROW 1
# ══════════════════════════════════════════════
st.markdown('<div class="sec-label">📉 REVENUE ANALYTICS — LIVE CHARTS</div>', unsafe_allow_html=True)
c1, c2 = st.columns([2, 1])

with c1:
    df_s = df.sort_values("timestamp").copy()
    df_s["cumrev"] = df_s["price"].cumsum()

    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(
        x=df_s["time"], y=df_s["cumrev"],
        name="Cumulative Revenue",
        mode="lines+markers",
        line=dict(color="#f5c842", width=2.5, shape="spline"),
        marker=dict(size=5, color="#f5c842"),
        fill="tozeroy", fillcolor="rgba(245,200,66,0.07)",
    ))
    fig_line.add_trace(go.Bar(
        x=df_s["time"], y=df_s["price"],
        name="Order Value",
        marker_color="rgba(56,182,245,0.45)",
        yaxis="y2",
    ))
    layout = dict(**BASE_LAYOUT)
    layout["yaxis2"] = dict(
        title="Order ₹", overlaying="y", side="right",
        color="#38b6f5", gridcolor="rgba(0,0,0,0)",
    )
    layout["title"] = dict(text="📈 Cumulative Revenue + Per-Order Value", font=dict(color="white", size=12), x=0)
    layout["height"] = 300
    layout["xaxis"]["tickangle"] = -30
    layout["legend"] = dict(orientation="h", y=-0.28, font=dict(color="#8899b5", size=9), bgcolor="rgba(0,0,0,0)")
    layout["hovermode"] = "x unified"
    fig_line.update_layout(**layout)
    st.plotly_chart(fig_line, use_container_width=True, config={"displayModeBar": False})

with c2:
    city_df = city_rev.reset_index()
    city_df.columns = ["City", "Revenue"]
    bar_c = []
    for city in city_df["City"]:
        w = wc.get(city, {})
        cls = classify(w.get("desc","Clear"), w.get("temp",30))
        bar_c.append("#38b6f5" if cls=="rain" else "#ff6b35" if cls=="heat" else "#2ecc9a")

    fig_city = go.Figure(go.Bar(
        x=city_df["Revenue"], y=city_df["City"],
        orientation="h",
        marker_color=bar_c,
        text=[f"₹{v:,}" for v in city_df["Revenue"]],
        textposition="outside",
        textfont=dict(color="#e8edf5", size=9),
    ))
    layout2 = dict(**BASE_LAYOUT)
    layout2["title"] = dict(text="🏙️ Revenue by City (colour = weather)", font=dict(color="white", size=12), x=0)
    layout2["height"] = 300
    layout2["yaxis"] = dict(**BASE_LAYOUT["yaxis"], autorange="reversed")
    layout2["xaxis"] = dict(**BASE_LAYOUT["xaxis"], title="Revenue ₹")
    fig_city.update_layout(**layout2)
    st.plotly_chart(fig_city, use_container_width=True, config={"displayModeBar": False})


# ══════════════════════════════════════════════
#  CHARTS ROW 2
# ══════════════════════════════════════════════
c3, c4, c5 = st.columns(3)

with c3:
    prod_df = prod_rev.reset_index()
    prod_df.columns = ["Product", "Revenue"]
    fig_donut = go.Figure(go.Pie(
        labels=prod_df["Product"], values=prod_df["Revenue"],
        hole=0.55,
        marker=dict(colors=CHART_COLORS[:len(prod_df)], line=dict(color="#060d1a", width=2)),
        textinfo="percent",
        textfont=dict(size=9, color="white"),
        hovertemplate="<b>%{label}</b><br>₹%{value:,}<br>%{percent}<extra></extra>",
    ))
    fig_donut.add_annotation(
        text=f"₹{total_rev:,}", x=0.5, y=0.5, showarrow=False,
        font=dict(size=11, color="#f5c842", family="Bebas Neue"),
    )
    layout3 = dict(**BASE_LAYOUT)
    layout3["title"]  = dict(text="🎯 Product Revenue Share", font=dict(color="white", size=12), x=0)
    layout3["height"] = 300
    layout3["showlegend"] = True
    layout3["legend"] = dict(font=dict(size=7), orientation="v", x=1.02, bgcolor="rgba(0,0,0,0)")
    fig_donut.update_layout(**layout3)
    st.plotly_chart(fig_donut, use_container_width=True, config={"displayModeBar": False})

with c4:
    c_names, temps, feels_l, bcolors = [], [], [], []
    for city in CITIES:
        w    = wc.get(city, {})
        temp = w.get("temp", 30)
        cls  = classify(w.get("desc","Clear"), temp)
        c_names.append(city)
        temps.append(temp)
        feels_l.append(w.get("feels", temp))
        bcolors.append("#38b6f5" if cls=="rain" else "#ff6b35" if cls=="heat" else "#2ecc9a" if cls=="clear" else "#6688aa")

    fig_temp = go.Figure()
    fig_temp.add_trace(go.Bar(
        x=c_names, y=temps, name="Temp °C",
        marker_color=bcolors,
        text=[f"{t}°" for t in temps],
        textposition="outside",
        textfont=dict(color="white", size=9),
    ))
    fig_temp.add_trace(go.Scatter(
        x=c_names, y=feels_l, name="Feels Like",
        mode="lines+markers",
        line=dict(color="#f5c842", dash="dot", width=1.5),
        marker=dict(size=5, color="#f5c842"),
    ))
    fig_temp.add_hline(
        y=37, line_dash="dot", line_color="#e8304a",
        annotation_text="🔥 Heat Risk 37°C",
        annotation_font_color="#e8304a",
        annotation_position="top right",
    )
    layout4 = dict(**BASE_LAYOUT)
    layout4["title"]  = dict(text="🌡️ Live City Temps  🔵 Rain · 🟠 Heat · 🟢 Clear", font=dict(color="white", size=11), x=0)
    layout4["height"] = 300
    layout4["xaxis"] = {**BASE_LAYOUT["xaxis"], "tickangle": -35}
    layout4["yaxis"]  = dict(**BASE_LAYOUT["yaxis"], title="°C")
    layout4["legend"] = dict(orientation="h", y=-0.3, font=dict(color="#8899b5", size=9), bgcolor="rgba(0,0,0,0)")
    fig_temp.update_layout(**layout4)
    st.plotly_chart(fig_temp, use_container_width=True, config={"displayModeBar": False})

with c5:
    city_o = df.groupby("city").size().reset_index(name="Orders")
    city_r = df.groupby("city")["price"].sum().reset_index(name="Revenue")
    city_m = city_o.merge(city_r, on="city")

    fig_bubble = go.Figure(go.Scatter(
        x=city_m["Orders"], y=city_m["Revenue"],
        mode="markers+text",
        text=city_m["city"],
        textposition="top center",
        textfont=dict(color="#e8edf5", size=8),
        marker=dict(
            size=city_m["Orders"] * 6,
            color=city_m["Revenue"],
            colorscale=[[0,"#0b1628"],[0.5,"#38b6f5"],[1,"#f5c842"]],
            showscale=True,
            colorbar=dict(thickness=6, tickfont=dict(size=7, color="#8899b5")),
            line=dict(color="#060d1a", width=1),
        ),
        hovertemplate="<b>%{text}</b><br>Orders: %{x}<br>Revenue: ₹%{y:,}<extra></extra>",
    ))
    layout5 = dict(**BASE_LAYOUT)
    layout5["title"]  = dict(text="🫧 City Orders vs Revenue", font=dict(color="white", size=12), x=0)
    layout5["height"] = 300
    layout5["xaxis"]  = dict(**BASE_LAYOUT["xaxis"], title="Order Count")
    layout5["yaxis"]  = dict(**BASE_LAYOUT["yaxis"], title="Revenue ₹")
    fig_bubble.update_layout(**layout5)
    st.plotly_chart(fig_bubble, use_container_width=True, config={"displayModeBar": False})


# ══════════════════════════════════════════════
#  BOTTOM: ORDER STREAM + LEADERBOARD
# ══════════════════════════════════════════════
st.markdown('<div class="sec-label">📋 LIVE ORDER STREAM + PRODUCT LEADERBOARD</div>', unsafe_allow_html=True)
b1, b2 = st.columns([2, 1])

with b1:
    disp = df.tail(15).iloc[::-1].copy()
    disp["Revenue"] = disp["price"].apply(lambda x: f"₹{x:,}")
    disp["WX"] = disp["city"].apply(lambda c: w_emoji(classify(
        wc.get(c,{}).get("desc","Clear"), wc.get(c,{}).get("temp",30)
    )))
    st.dataframe(
        disp[["time","product","Revenue","city","WX"]].rename(
            columns={"time":"TIME","product":"PRODUCT","city":"CITY"}
        ),
        use_container_width=True, height=330, hide_index=True,
    )

with b2:
    lb = (
        df.groupby("product")
        .agg(Orders=("price","count"), Revenue=("price","sum"))
        .sort_values("Revenue", ascending=False)
        .reset_index()
    )
    lb["Share"]   = (lb["Revenue"] / lb["Revenue"].sum() * 100).round(1).astype(str) + "%"
    lb["Revenue"] = lb["Revenue"].apply(lambda x: f"₹{x:,}")
    lb.insert(0, "#", range(1, len(lb)+1))
    lb = lb.rename(columns={"product":"PRODUCT"})
    st.dataframe(lb, use_container_width=True, height=330, hide_index=True)


# ══════════════════════════════════════════════
#  FOOTER
# ══════════════════════════════════════════════
st.markdown("""
<div class="dash-footer">
  🎯 SALES COMMAND CENTER · LIVE REVENUE PULSE WAR ROOM
  &nbsp;|&nbsp; WEATHER: OPENWEATHERMAP LIVE API (37b1…)
  &nbsp;|&nbsp; AUTO-REFRESH: 5s &nbsp;|&nbsp; SALE ENGINE: 30s
  &nbsp;|&nbsp; BUILT FOR COMMAND-LEVEL DECISIONS
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  AUTO-REFRESH
# ══════════════════════════════════════════════
time.sleep(5)
st.rerun()