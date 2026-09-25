"""Company income, revenue, expense, profit, and loss dashboard.

Start it with: streamlit run moneydashboard.py
"""

from datetime import date

import pandas as pd
import importlib


st = importlib.import_module("streamlit")


st.set_page_config(page_title="Money Dashboard", page_icon="💰", layout="wide")
st.title("💰 Company Money Dashboard")
st.write("Enter monthly figures or upload a CSV to visualize company performance.")


def currency(value):
	return f"${value:,.2f}"


with st.sidebar:
	st.header("Data source")
	uploaded = st.file_uploader(
		"Upload CSV with date, revenue, expenses, and income columns",
		type="csv",
	)

	if uploaded is not None:
		data = pd.read_csv(uploaded)
		required = {"date", "revenue", "expenses", "income"}
		missing = required.difference(data.columns)
		if missing:
			st.error("Missing columns: " + ", ".join(sorted(missing)))
			st.stop()
	else:
		st.header("Add monthly data")
		count = int(st.number_input("Number of months", min_value=1, max_value=24, value=6))
		rows = []
		for index in range(count):
			st.caption(f"Month {index + 1}")
			rows.append(
				{
					"date": st.date_input("Date", date.today(), key=f"date_{index}"),
					"revenue": st.number_input("Revenue", min_value=0.0, step=100.0, key=f"revenue_{index}"),
					"expenses": st.number_input("Expenses", min_value=0.0, step=100.0, key=f"expenses_{index}"),
					"income": st.number_input("Other income", min_value=0.0, step=100.0, key=f"income_{index}"),
				}
			)
		data = pd.DataFrame(rows)

data["date"] = pd.to_datetime(data["date"], errors="coerce")
for column in ("revenue", "expenses", "income"):
	data[column] = pd.to_numeric(data[column], errors="coerce").fillna(0)
data = data.dropna(subset=["date"]).sort_values("date")
data["total_income"] = data["revenue"] + data["income"]
data["profit"] = data["total_income"] - data["expenses"]
data["loss"] = data["profit"].clip(upper=0).abs()
data["margin"] = (data["profit"] / data["total_income"].replace(0, pd.NA) * 100).fillna(0)

total_income = data["total_income"].sum()
total_profit = data["profit"].sum()
cards = st.columns(5)
cards[0].metric("Revenue", currency(data["revenue"].sum()))
cards[1].metric("Total income", currency(total_income))
cards[2].metric("Expenses", currency(data["expenses"].sum()))
cards[3].metric("Profit", currency(total_profit))
cards[4].metric("Loss", currency(data["loss"].sum()))

st.subheader("Financial overview")
plot_data = data.melt(
	id_vars="date",
	value_vars=["revenue", "total_income", "expenses", "profit", "loss"],
	var_name="Metric",
	value_name="Amount",
)
st.line_chart(plot_data, x="date", y="Amount", color="Metric", use_container_width=True)

left, right = st.columns(2)
with left:
	st.bar_chart(data, x="date", y=["total_income", "expenses"], use_container_width=True)
with right:
	st.area_chart(data, x="date", y="profit", use_container_width=True)

st.subheader("Detailed figures")
table = data[["date", "revenue", "income", "expenses", "total_income", "profit", "loss", "margin"]].copy()
table["date"] = table["date"].dt.strftime("%Y-%m-%d")
st.dataframe(table, use_container_width=True)
