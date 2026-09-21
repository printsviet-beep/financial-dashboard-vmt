import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Financial Dashboard VMT",
    page_icon="📊",
    layout="wide"
)

st.title("📊 FINANCIAL HEALTH MONITOR – BTC VMT")

st.write("Hệ thống phân tích tài chính BTC VMT")

st.divider()

st.subheader("📁 Bước 1: Upload báo cáo tài chính")

uploaded_file = st.file_uploader(
    "Chọn file Excel báo cáo tài chính",
    type=["xlsx", "xls"]
)

if uploaded_file is not None:

    st.success("Đã nhận file Excel!")

    excel_file = pd.ExcelFile(uploaded_file)

    st.subheader("📑 Các sheet trong file")

    sheet_names = excel_file.sheet_names

    st.write(sheet_names)

    selected_sheet = st.selectbox(
        "Chọn sheet muốn xem",
        sheet_names
    )

    df = pd.read_excel(
        uploaded_file,
        sheet_name=selected_sheet
    )

    st.subheader(f"📋 Dữ liệu: {selected_sheet}")

    st.dataframe(
        df,
        use_container_width=True
    )
