from __future__ import annotations

import pandas as pd
import streamlit as st

from core.analysis import build_report_table
from core.utils import build_pdf_report, dataframe_to_csv_bytes


def render_reports_page(filtered_df: pd.DataFrame) -> None:
    st.markdown("## Reports & Downloads")
    report_df = build_report_table(filtered_df)
    csv_bytes = dataframe_to_csv_bytes(filtered_df)
    pdf_bytes = build_pdf_report(report_df, filtered_df)
    col1, col2 = st.columns(2)
    col1.download_button(
        "Download filtered data (CSV)",
        data=csv_bytes,
        file_name="traffic_violation_filtered_report.csv",
        mime="text/csv",
        use_container_width=True,
    )
    col2.download_button(
        "Download summary report (PDF)",
        data=pdf_bytes,
        file_name="traffic_violation_summary.pdf",
        mime="application/pdf",
        use_container_width=True,
    )
    st.dataframe(
        report_df.rename(columns={"metric": "Metric", "value": "Value"}),
        use_container_width=True,
        hide_index=True,
    )
