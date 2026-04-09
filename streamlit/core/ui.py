from __future__ import annotations

from collections.abc import Sequence

import pandas as pd
import streamlit as st

from core.app_config import METRIC_STYLES, NAV_ITEMS


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(180deg, #f4f7fb 0%, #eef3f9 100%);
            color: #0f172a;
        }
        .stApp * {
            box-sizing: border-box;
        }
        .block-container {
            padding-top: 1.45rem;
            padding-bottom: 2.1rem;
        }
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #081120 0%, #07172a 100%);
            border-right: 1px solid rgba(255, 255, 255, 0.06);
        }
        section[data-testid="stSidebar"] * {
            color: #e2e8f0;
        }
        [data-testid="stSidebarNav"] {
            display: none;
        }
        div[role="radiogroup"] > label {
            background: transparent;
            border: 1px solid transparent;
            border-radius: 14px;
            padding: 0.7rem 0.8rem;
            margin-bottom: 0.32rem;
        }
        div[role="radiogroup"] > label:hover {
            background: rgba(255, 255, 255, 0.06);
        }
        div[role="radiogroup"] label[data-baseweb="radio"] > div:first-child {
            display: none;
        }
        div[role="radiogroup"] label[data-baseweb="radio"] span {
            font-size: 1.02rem;
            font-weight: 600;
            color: #e2e8f0;
        }
        .status-card {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 18px;
            padding: 1rem;
            margin-top: 2rem;
        }
        section[data-testid="stSidebar"] [data-testid="stFileUploader"] {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 0.45rem;
        }
        section[data-testid="stSidebar"] [data-testid="stFileUploader"] section {
            padding: 0.5rem;
            min-height: auto;
        }
        section[data-testid="stSidebar"] [data-testid="stFileUploader"] small {
            font-size: 0.72rem;
        }
        .topbar {
            display: flex;
            align-items: center;
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(15, 23, 42, 0.08);
            border-radius: 22px;
            padding: 0.7rem 0.95rem 0.35rem 0.95rem;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.05);
            margin-bottom: 1rem;
        }
        .topbar .stTextInput {
            width: 100%;
        }
        .topbar .stTextInput > div {
            width: 100%;
        }
        .topbar .stTextInput input {
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 14px;
            color: #0f172a;
            font-size: 0.95rem;
            padding: 0.85rem 1rem;
        }
        .filter-shell {
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(15, 23, 42, 0.08);
            border-radius: 20px;
            padding: 1rem 1rem 0.25rem 1rem;
            box-shadow: 0 10px 26px rgba(15, 23, 42, 0.05);
            margin-bottom: 1rem;
        }
        .filter-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 0.8rem;
        }
        .hero-banner {
            background: linear-gradient(115deg, rgba(255,255,255,0.96) 0%, rgba(243,244,255,0.95) 45%, rgba(191,219,254,0.95) 100%);
            border: 1px solid rgba(15, 23, 42, 0.08);
            border-radius: 24px;
            padding: 1.75rem 1.6rem 1.7rem 1.6rem;
            box-shadow: 0 16px 36px rgba(15, 23, 42, 0.08);
            margin-bottom: 1.15rem;
        }
        .hero-title {
            font-size: 1.8rem;
            font-weight: 800;
            line-height: 1.22;
            margin: 0 0 0.65rem 0;
        }
        .hero-copy {
            color: #334155;
            max-width: 44rem;
            font-size: 1rem;
            line-height: 1.65;
            margin: 0;
        }
        .metric-card {
            color: white;
            border-radius: 20px;
            padding: 1rem 1.1rem;
            box-shadow: 0 16px 34px rgba(15, 23, 42, 0.10);
            min-height: 140px;
        }
        .metric-icon {
            width: 50px;
            height: 50px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            background: rgba(255, 255, 255, 0.16);
            margin-bottom: 0.7rem;
        }
        .metric-label {
            font-size: 0.95rem;
            opacity: 0.9;
        }
        .metric-value {
            font-size: 2rem;
            font-weight: 800;
            margin: 0.2rem 0;
        }
        .metric-note {
            font-size: 0.9rem;
            opacity: 0.88;
        }
        .panel-card {
            background: rgba(255, 255, 255, 0.94);
            border: 1px solid rgba(15, 23, 42, 0.08);
            border-radius: 20px;
            padding: 0.7rem 0.8rem 0.2rem 0.8rem;
            box-shadow: 0 16px 36px rgba(15, 23, 42, 0.06);
            width: 100%;
        }
        .panel-title {
            font-size: 1.12rem;
            font-weight: 700;
            margin: 0.2rem 0 0.9rem 0.25rem;
            color: #0f172a;
        }
        .section-shell {
            background: linear-gradient(135deg, rgba(255,255,255,0.98) 0%, rgba(241,245,249,0.95) 100%);
            border: 1px solid rgba(148, 163, 184, 0.20);
            border-radius: 22px;
            padding: 1rem 1.15rem;
            box-shadow: 0 18px 40px rgba(15, 23, 42, 0.06);
            margin: 1.25rem 0 0.95rem 0;
        }
        .section-kicker {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.28rem 0.7rem;
            border-radius: 999px;
            background: rgba(37, 99, 235, 0.10);
            color: #1d4ed8;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            margin-bottom: 0.65rem;
        }
        .section-heading-row {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin-bottom: 0.4rem;
        }
        .section-icon {
            width: 44px;
            height: 44px;
            border-radius: 14px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
            color: #1d4ed8;
            flex-shrink: 0;
        }
        .section-title {
            font-size: 1.32rem;
            font-weight: 800;
            color: #0f172a;
            margin: 0;
            overflow-wrap: anywhere;
        }
        .section-copy {
            color: #475569;
            line-height: 1.6;
            margin: 0;
            max-width: 58rem;
            overflow-wrap: anywhere;
        }
        .analysis-card {
            background: linear-gradient(180deg, rgba(255,255,255,0.98) 0%, rgba(248,250,252,0.96) 100%);
            border: 1px solid rgba(148, 163, 184, 0.20);
            border-radius: 18px;
            padding: 1rem 1rem 0.95rem 1rem;
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.05);
        }
        .analysis-card-head {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            margin-bottom: 0.45rem;
        }
        .analysis-card-icon {
            width: 38px;
            height: 38px;
            border-radius: 12px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 1.05rem;
            background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
            color: #1d4ed8;
            flex-shrink: 0;
        }
        .analysis-label {
            font-size: 0.82rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #64748b;
            font-weight: 700;
            margin-bottom: 0.4rem;
        }
        .analysis-value {
            font-size: 1.32rem;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 0.35rem;
            overflow-wrap: anywhere;
        }
        .analysis-note {
            color: #475569;
            line-height: 1.55;
            font-size: 0.94rem;
            overflow-wrap: anywhere;
        }
        .analysis-text-panel {
            background: rgba(255, 255, 255, 0.96);
            border: 1px solid rgba(15, 23, 42, 0.08);
            border-radius: 20px;
            padding: 1.1rem 1.2rem;
            box-shadow: 0 14px 34px rgba(15, 23, 42, 0.05);
            margin-bottom: 1rem;
        }
        .analysis-panel-title {
            font-size: 1.08rem;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 0.55rem;
        }
        .analysis-panel-head {
            display: flex;
            align-items: center;
            gap: 0.7rem;
            margin-bottom: 0.55rem;
        }
        .analysis-panel-icon {
            width: 40px;
            height: 40px;
            border-radius: 12px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 1.05rem;
            background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%);
            color: #4338ca;
            flex-shrink: 0;
        }
        .analysis-bullet {
            color: #334155;
            line-height: 1.65;
            margin: 0.28rem 0;
            overflow-wrap: anywhere;
        }
        div[data-testid="column"] {
            width: 100%;
            min-width: 0;
            flex: 1 1 0;
        }
        div[data-testid="column"] > div {
            width: 100%;
        }
        div[data-testid="stHorizontalBlock"] {
            gap: 1rem;
        }
        div[data-testid="stPlotlyChart"] {
            width: 100%;
            overflow: hidden;
        }
        div[data-testid="stPlotlyChart"] > div {
            width: 100% !important;
        }
        .stDataFrame,
        [data-testid="stDataFrame"] {
            width: 100%;
        }
        @media (max-width: 1100px) {
            .hero-title {
                font-size: 1.55rem;
            }
            .metric-card {
                min-height: unset;
            }
            .section-heading-row {
                align-items: flex-start;
            }
            div[data-testid="stHorizontalBlock"] {
                flex-wrap: wrap;
            }
            div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
                flex: 1 1 260px;
            }
        }
        @media (max-width: 768px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }
            .hero-banner,
            .filter-shell,
            .section-shell,
            .panel-card,
            .analysis-card,
            .analysis-text-panel,
            .status-card {
                border-radius: 18px;
            }
            .hero-banner,
            .filter-shell,
            .section-shell {
                padding-left: 1rem;
                padding-right: 1rem;
            }
            .hero-title {
                font-size: 1.35rem;
            }
            .hero-copy,
            .section-copy,
            .analysis-note,
            .analysis-bullet {
                font-size: 0.95rem;
            }
            .metric-value,
            .analysis-value {
                font-size: 1.15rem;
            }
            .section-heading-row,
            .analysis-card-head,
            .analysis-panel-head {
                gap: 0.6rem;
            }
            .section-icon,
            .analysis-card-icon,
            .analysis-panel-icon,
            .metric-icon {
                transform: scale(0.94);
                transform-origin: left center;
            }
            div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
                flex-basis: 100% !important;
                min-width: 100%;
            }
        }
        .progress-row {
            margin-bottom: 1rem;
        }
        .progress-line {
            height: 10px;
            border-radius: 999px;
            background: #e2e8f0;
            overflow: hidden;
            margin-top: 0.35rem;
        }
        .progress-fill {
            height: 100%;
            border-radius: 999px;
        }
        .insight-card {
            border-radius: 16px;
            padding: 1rem;
            margin-bottom: 0.8rem;
            border: 1px solid rgba(15, 23, 42, 0.08);
        }
        .insight-warn {
            background: linear-gradient(180deg, #fff1f2 0%, #ffe4e6 100%);
        }
        .insight-info {
            background: linear-gradient(180deg, #eff6ff 0%, #dbeafe 100%);
        }
        .home-card {
            background: rgba(255, 255, 255, 0.95);
            border: 1px solid rgba(15, 23, 42, 0.08);
            border-radius: 18px;
            padding: 1.1rem;
            box-shadow: 0 14px 32px rgba(15, 23, 42, 0.06);
            min-height: 170px;
        }
        .home-card-head {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 0.9rem;
        }
        .home-card-icon {
            width: 44px;
            height: 44px;
            border-radius: 12px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
            color: #1d4ed8;
            flex-shrink: 0;
        }
        .home-card-title {
            margin: 0;
            color: #0f172a;
        }
        .home-feature-list {
            margin: 0;
            padding-left: 1.1rem;
            color: #334155;
        }
        .home-feature-list li {
            margin-bottom: 0.48rem;
            line-height: 1.45;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def render_dashboard_header() -> None:
    st.markdown(
        """
        <div class="hero-banner">
            <div class="hero-title">Smart Traffic Violation Summary Dashboard &#128202;</div>
            <div class="hero-copy">An icon-led summary dashboard for understanding traffic patterns, hotspots, speed behavior, payments, and category trends across the dataset.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_analytics_header() -> None:
    st.markdown(
        """
        <div class="hero-banner">
            <div class="hero-title">&#128200; Advanced Analytics</div>
            <div class="hero-copy">A text-first interpretation layer that turns filtered traffic records into short, readable findings for operational review and stakeholder reporting.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_dashboard_filters(df, title: str = "Dashboard Filters"):
    st.markdown('<div class="filter-shell">', unsafe_allow_html=True)
    st.markdown(f'<div class="filter-title">{title}</div>', unsafe_allow_html=True)

    min_date = df["date"].min().date()
    max_date = df["date"].max().date()
    col1, col2, col3 = st.columns([1.2, 1, 1])

    date_range = col1.date_input(
        "Date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        key="dashboard_date_range",
    )

    if isinstance(date_range, Sequence) and not isinstance(date_range, (str, bytes)) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date = end_date = date_range if date_range else min_date

    locations = col2.multiselect(
        "Location",
        options=sorted(df["location"].dropna().unique().tolist()),
        key="dashboard_locations",
    )
    violation_types = col3.multiselect(
        "Violation type",
        options=sorted(df["violation_type"].dropna().unique().tolist()),
        key="dashboard_violation_types",
    )

    st.markdown("</div>", unsafe_allow_html=True)
    return start_date, end_date, locations, violation_types

def render_sidebar_nav() -> str:
    page = st.sidebar.radio("Navigation", NAV_ITEMS, label_visibility="collapsed")
    st.sidebar.markdown(
        """
        <div class="status-card">
            <div style="font-size:1rem; font-weight:700; color:white; margin-bottom:0.35rem;">System Status</div>
            <div style="color:#cbd5e1; font-size:0.9rem;">Insights, filters, reports, and prediction tools are available.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    return page

def render_metric_card(style_key: str, label: str, value: str, note: str) -> None:
    style = METRIC_STYLES[style_key]
    st.markdown(
        f"""
        <div class="metric-card" style="background:{style['bg']};">
            <div class="metric-icon">{style['icon']}</div>
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_top_violation_panel(type_df: pd.DataFrame) -> None:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Top Violation Types</div>', unsafe_allow_html=True)
    if type_df.empty:
        st.info("No violation data available.")
    else:
        total = max(int(type_df["count"].sum()), 1)
        colors = ["#ef4444", "#f97316", "#f59e0b", "#22c55e", "#3b82f6"]
        for idx, row in enumerate(type_df.head(5).itertuples(index=False)):
            share = (row.count / total) * 100
            color = colors[idx % len(colors)]
            st.markdown(
                f"""
                <div class="progress-row">
                    <div style="display:flex; justify-content:space-between; gap:1rem; font-weight:600; color:#0f172a;">
                        <span>{row.violation_type}</span>
                        <span>{row.count} ({share:.1f}%)</span>
                    </div>
                    <div class="progress-line">
                        <div class="progress-fill" style="width:{share:.1f}%; background:{color};"></div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True)

def render_ai_insights(patterns: dict[str, object], risk_df: pd.DataFrame) -> None:
    top_area = risk_df.iloc[0]["location"] if not risk_df.empty else "N/A"
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">AI Insights & Recommendations</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="insight-card insight-warn">
            <div style="font-weight:700; margin-bottom:0.35rem;">Peak Violation Hours</div>
            <div>Violations are most active around <b>{patterns['peak_hour']}</b>. Consider increasing patrol coverage during this window.</div>
        </div>
        <div class="insight-card insight-info">
            <div style="font-weight:700; margin-bottom:0.35rem;">High Risk Focus Area</div>
            <div><b>{top_area}</b> appears as a leading risk zone in the current filtered view. This area may benefit from more monitoring or signage.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

def render_recent_violations(df: pd.DataFrame) -> None:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Recent Violations</div>', unsafe_allow_html=True)
    recent = df.sort_values(["date", "time"], ascending=[False, False]).head(6).copy()
    if recent.empty:
        st.info("No recent records available.")
    else:
        id_col = "Violation_ID" if "Violation_ID" in recent.columns else None
        if id_col is None:
            recent.insert(0, "Violation_ID", [f"TV{1000+i}" for i in range(len(recent))])
            id_col = "Violation_ID"
        recent_table = recent[[id_col, "location", "violation_type", "time"]].rename(
            columns={id_col: "ID", "location": "Location", "violation_type": "Type", "time": "Time"}
        )
        if "Fine_Paid" in recent.columns:
            recent_table["Status"] = recent["Fine_Paid"].replace({"Yes": "Paid", "No": "Pending"})
        st.dataframe(recent_table, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_chart_panel(fig) -> None:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_section_header(kicker: str, icon: str, title: str, copy: str) -> None:
    st.markdown(
        f"""
        <div class="section-shell">
            <div class="section-kicker">{kicker}</div>
            <div class="section-heading-row">
                <div class="section-icon">{icon}</div>
                <div class="section-title">{title}</div>
            </div>
            <p class="section-copy">{copy}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_analysis_cards(cards: list[dict[str, str]]) -> None:
    columns = st.columns(len(cards))
    for column, card in zip(columns, cards):
        with column:
            st.markdown(
                f"""
                <div class="analysis-card">
                    <div class="analysis-card-head">
                        <div class="analysis-card-icon">{card.get('icon', '&#128202;')}</div>
                        <div class="analysis-label">{card['label']}</div>
                    </div>
                    <div class="analysis-value">{card['value']}</div>
                    <div class="analysis-note">{card['note']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

def render_analysis_text_panel(title: str, bullets: list[str], icon: str = "&#128221;") -> None:
    bullet_html = "".join(f'<div class="analysis-bullet">{item}</div>' for item in bullets)
    st.markdown(
        f"""
        <div class="analysis-text-panel">
            <div class="analysis-panel-head">
                <div class="analysis-panel-icon">{icon}</div>
                <div class="analysis-panel-title">{title}</div>
            </div>
            {bullet_html}
        </div>
        """,
        unsafe_allow_html=True,
    )



