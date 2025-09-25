💰 Personal Finance Manager (with Visualization)

A Python-based Personal Finance Manager that helps you track income and expenses, generate summaries, and visualize your finances with charts.

🚀 Features

Add income and expenses with categories and dates.

View your current balance (income – expenses).

Generate category breakdowns (pie charts of expenses).

Plot monthly income vs expenses trendline.

Save & load transactions via CSV file.

Simple command-line interface.

🛠️ Tech Stack

Python 3.x

Pandas → data handling

Matplotlib / Plotly → visualization

CSV → file storage

📊 Example Visualizations

Pie Chart → Expenses by category

Line Chart → Monthly income vs expenses

(Screenshots/plots will appear here once generated)

📂 Project Structure
finance_manager/
│── finance_manager.py   # Main program
│── expenses.csv         # Saved transactions
│── README.md            # Project documentation

▶️ Usage

Clone this repo:

git clone https://github.com/yourusername/finance-manager.git
cd finance-manager


Install dependencies:

pip install pandas matplotlib


Run the program:

python finance_manager.py

📌 Example Transactions
type,item,amount,category,date,due date
income,Salary,2000,Job,2025-09-01,
expense,Groceries,120,Food,2025-09-03,2025-09-04
expense,Electric Bill,60,Utilities,2025-09-04,2025-09-10

🔮 Future Improvements

Add budget goals and alerts.

Export charts as images.

GUI or web dashboard version.
