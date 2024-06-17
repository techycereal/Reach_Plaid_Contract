import pandas as pd
import numpy as np
from calendar import monthrange
import sys
import json

# data = [{"date":"2024-05-24","category":"Payment","amount":25},{"date":"2024-05-24","category":"Travel","amount":5.4},{"date":"2024-05-22","category":"Travel","amount":-500},{"date":"2024-05-21","category":"Food and Drink","amount":12},{"date":"2024-05-21","category":"Food and Drink","amount":4.33},{"date":"2024-05-20","category":"Food and Drink","amount":89.4},{"date":"2024-05-19","category":"Transfer","amount":-4.22},{"date":"2024-05-07","category":"Travel","amount":6.33},{"date":"2024-04-24","category":"Payment","amount":25},{"date":"2024-04-24","category":"Uncategorized","amount":5.4},{"date":"2024-04-22","category":"Travel","amount":-500},{"date":"2024-04-21","category":"Food and Drink","amount":12},{"date":"2024-04-21","category":"Food and Drink","amount":4.33},{"date":"2024-04-20","category":"Uncategorized","amount":89.4},{"date":"2024-04-19","category":"Uncategorized","amount":-4.22},{"date":"2024-04-07","category":"Uncategorized","amount":6.33},{"date":"2024-03-25","category":"Payment","amount":25},{"date":"2024-03-25","category":"Uncategorized","amount":5.4},{"date":"2024-03-23","category":"Travel","amount":-500},{"date":"2024-03-22","category":"Food and Drink","amount":12},{"date":"2024-03-22","category":"Food and Drink","amount":4.33},{"date":"2024-03-21","category":"Uncategorized","amount":89.4},{"date":"2024-03-20","category":"Uncategorized","amount":-4.22},{"date":"2024-03-08","category":"Uncategorized","amount":6.33},{"date":"2024-02-24","category":"Payment","amount":25},{"date":"2024-02-24","category":"Uncategorized","amount":5.4},{"date":"2024-02-22","category":"Travel","amount":-500},{"date":"2024-02-21","category":"Food and Drink","amount":12},{"date":"2024-02-21","category":"Food and Drink","amount":4.33},{"date":"2024-02-20","category":"Uncategorized","amount":89.4},{"date":"2024-02-19","category":"Uncategorized","amount":-4.22},{"date":"2024-02-07","category":"Uncategorized","amount":6.33},{"date":"2024-01-25","category":"Payment","amount":25},{"date":"2024-01-25","category":"Uncategorized","amount":5.4},{"date":"2024-01-23","category":"Travel","amount":-500},{"date":"2024-01-22","category":"Food and Drink","amount":12},{"date":"2024-01-22","category":"Food and Drink","amount":4.33},{"date":"2024-01-21","category":"Uncategorized","amount":89.4},{"date":"2024-01-20","category":"Uncategorized","amount":-4.22},{"date":"2024-01-08","category":"Uncategorized","amount":6.33},{"date":"2023-12-26","category":"Payment","amount":25},{"date":"2023-12-26","category":"Uncategorized","amount":5.4},{"date":"2023-12-24","category":"Travel","amount":-500},{"date":"2023-12-23","category":"Food and Drink","amount":12},{"date":"2023-12-23","category":"Food and Drink","amount":4.33},{"date":"2023-12-22","category":"Uncategorized","amount":89.4},{"date":"2023-12-21","category":"Uncategorized","amount":-4.22},{"date":"2023-12-09","category":"Uncategorized","amount":6.33},{"date":"2023-11-26","category":"Payment","amount":25},{"date":"2023-11-26","category":"Uncategorized","amount":5.4},{"date":"2023-11-24","category":"Travel","amount":-500},{"date":"2023-11-23","category":"Food and Drink","amount":12},{"date":"2023-11-23","category":"Food and Drink","amount":4.33},{"date":"2023-11-22","category":"Uncategorized","amount":89.4},{"date":"2023-11-21","category":"Uncategorized","amount":-4.22},{"date":"2023-11-09","category":"Uncategorized","amount":6.33},{"date":"2023-10-27","category":"Payment","amount":25},{"date":"2023-10-27","category":"Uncategorized","amount":5.4},{"date":"2023-10-25","category":"Travel","amount":-500},{"date":"2023-10-24","category":"Food and Drink","amount":12},{"date":"2023-10-24","category":"Food and Drink","amount":4.33},{"date":"2023-10-23","category":"Uncategorized","amount":89.4},{"date":"2023-10-22","category":"Uncategorized","amount":-4.22},{"date":"2023-10-10","category":"Uncategorized","amount":6.33},{"date":"2023-09-27","category":"Payment","amount":25},{"date":"2023-09-27","category":"Uncategorized","amount":5.4},{"date":"2023-09-25","category":"Travel","amount":-500},{"date":"2023-09-24","category":"Food and Drink","amount":12},{"date":"2023-09-24","category":"Food and Drink","amount":4.33},{"date":"2023-09-23","category":"Uncategorized","amount":89.4},{"date":"2023-09-22","category":"Uncategorized","amount":-4.22},{"date":"2023-09-10","category":"Uncategorized","amount":6.33},{"date":"2023-08-28","category":"Payment","amount":25},{"date":"2023-08-28","category":"Uncategorized","amount":5.4},{"date":"2023-08-26","category":"Travel","amount":-500},{"date":"2023-08-25","category":"Food and Drink","amount":12},{"date":"2023-08-25","category":"Food and Drink","amount":4.33},{"date":"2023-08-24","category":"Uncategorized","amount":89.4},{"date":"2023-08-23","category":"Uncategorized","amount":-4.22},{"date":"2023-08-11","category":"Uncategorized","amount":6.33},{"date":"2023-07-29","category":"Payment","amount":25},{"date":"2023-07-29","category":"Uncategorized","amount":5.4},{"date":"2023-07-27","category":"Travel","amount":-500},{"date":"2023-07-26","category":"Food and Drink","amount":12},{"date":"2023-07-26","category":"Food and Drink","amount":4.33},{"date":"2023-07-25","category":"Uncategorized","amount":89.4},{"date":"2023-07-24","category":"Uncategorized","amount":-4.22},{"date":"2023-07-12","category":"Uncategorized","amount":6.33},{"date":"2023-06-29","category":"Payment","amount":25},{"date":"2023-06-29","category":"Uncategorized","amount":5.4},{"date":"2023-06-27","category":"Travel","amount":-500},{"date":"2023-06-26","category":"Food and Drink","amount":12},{"date":"2023-06-26","category":"Food and Drink","amount":4.33},{"date":"2023-06-25","category":"Uncategorized","amount":89.4},{"date":"2023-06-24","category":"Uncategorized","amount":-4.22},{"date":"2023-06-12","category":"Uncategorized","amount":6.33},{"date":"2023-05-30","category":"Payment","amount":25},{"date":"2023-05-30","category":"Uncategorized","amount":5.4},{"date":"2023-05-28","category":"Travel","amount":-500},{"date":"2023-05-27","category":"Food and Drink","amount":12},{"date":"2023-05-27","category":"Food and Drink","amount":4.33},{"date":"2023-05-26","category":"Uncategorized","amount":89.4},{"date":"2023-05-25","category":"Uncategorized","amount":-4.22},{"date":"2023-05-13","category":"Uncategorized","amount":6.33},{"date":"2023-04-30","category":"Payment","amount":25},{"date":"2023-04-30","category":"Uncategorized","amount":5.4},{"date":"2023-04-28","category":"Travel","amount":-500},{"date":"2023-04-27","category":"Food and Drink","amount":12},{"date":"2023-04-27","category":"Food and Drink","amount":4.33},{"date":"2023-04-26","category":"Uncategorized","amount":89.4},{"date":"2023-04-25","category":"Uncategorized","amount":-4.22},{"date":"2023-04-13","category":"Uncategorized","amount":6.33},{"date":"2023-03-31","category":"Payment","amount":25},{"date":"2023-03-31","category":"Uncategorized","amount":5.4},{"date":"2023-03-29","category":"Travel","amount":-500},{"date":"2023-03-28","category":"Food and Drink","amount":12},{"date":"2023-03-28","category":"Food and Drink","amount":4.33},{"date":"2023-03-27","category":"Uncategorized","amount":89.4},{"date":"2023-03-26","category":"Uncategorized","amount":-4.22},{"date":"2023-03-14","category":"Uncategorized","amount":6.33},{"date":"2023-03-01","category":"Payment","amount":25},{"date":"2023-03-01","category":"Uncategorized","amount":5.4},{"date":"2023-02-27","category":"Travel","amount":-500},{"date":"2023-02-26","category":"Food and Drink","amount":12},{"date":"2023-02-26","category":"Food and Drink","amount":4.33},{"date":"2023-02-25","category":"Uncategorized","amount":89.4},{"date":"2023-02-24","category":"Uncategorized","amount":-4.22},{"date":"2023-02-12","category":"Uncategorized","amount":6.33},{"date":"2023-01-30","category":"Payment","amount":25},{"date":"2023-01-30","category":"Uncategorized","amount":5.4},{"date":"2023-01-28","category":"Travel","amount":-500},{"date":"2023-01-27","category":"Food and Drink","amount":12},{"date":"2023-01-27","category":"Food and Drink","amount":4.33},{"date":"2023-01-26","category":"Uncategorized","amount":89.4},{"date":"2023-01-25","category":"Uncategorized","amount":-4.22},{"date":"2023-01-13","category":"Uncategorized","amount":6.33},{"date":"2022-12-31","category":"Payment","amount":25},{"date":"2022-12-31","category":"Uncategorized","amount":5.4},{"date":"2022-12-29","category":"Travel","amount":-500},{"date":"2022-12-28","category":"Food and Drink","amount":12},{"date":"2022-12-28","category":"Food and Drink","amount":4.33},{"date":"2022-12-27","category":"Uncategorized","amount":89.4},{"date":"2022-12-26","category":"Uncategorized","amount":-4.22},{"date":"2022-12-14","category":"Uncategorized","amount":6.33},{"date":"2022-12-01","category":"Payment","amount":25},{"date":"2022-12-01","category":"Uncategorized","amount":5.4},{"date":"2022-11-29","category":"Travel","amount":-500},{"date":"2022-11-28","category":"Food and Drink","amount":12},{"date":"2022-11-28","category":"Food and Drink","amount":4.33},{"date":"2022-11-27","category":"Uncategorized","amount":89.4},{"date":"2022-11-26","category":"Uncategorized","amount":-4.22},{"date":"2022-11-14","category":"Uncategorized","amount":6.33},{"date":"2022-11-01","category":"Payment","amount":25},{"date":"2022-11-01","category":"Uncategorized","amount":5.4},{"date":"2022-10-30","category":"Travel","amount":-500},{"date":"2022-10-29","category":"Food and Drink","amount":12},{"date":"2022-10-29","category":"Food and Drink","amount":4.33},{"date":"2022-10-28","category":"Uncategorized","amount":89.4},{"date":"2022-10-27","category":"Uncategorized","amount":-4.22},{"date":"2022-10-15","category":"Uncategorized","amount":6.33},{"date":"2022-10-02","category":"Payment","amount":25},{"date":"2022-10-02","category":"Uncategorized","amount":5.4},{"date":"2022-09-30","category":"Travel","amount":-500},{"date":"2022-09-29","category":"Food and Drink","amount":12},{"date":"2022-09-29","category":"Food and Drink","amount":4.33},{"date":"2022-09-28","category":"Uncategorized","amount":89.4},{"date":"2022-09-27","category":"Uncategorized","amount":-4.22},{"date":"2022-09-15","category":"Uncategorized","amount":6.33},{"date":"2022-09-02","category":"Payment","amount":25},{"date":"2022-09-02","category":"Uncategorized","amount":5.4},{"date":"2022-08-31","category":"Travel","amount":-500},{"date":"2022-08-30","category":"Food and Drink","amount":12},{"date":"2022-08-30","category":"Food and Drink","amount":4.33},{"date":"2022-08-29","category":"Uncategorized","amount":89.4},{"date":"2022-08-28","category":"Uncategorized","amount":-4.22},{"date":"2022-08-16","category":"Uncategorized","amount":6.33},{"date":"2022-08-03","category":"Payment","amount":25},{"date":"2022-08-03","category":"Uncategorized","amount":5.4},{"date":"2022-08-01","category":"Travel","amount":-500},{"date":"2022-07-31","category":"Food and Drink","amount":12},{"date":"2022-07-31","category":"Food and Drink","amount":4.33},{"date":"2022-07-30","category":"Uncategorized","amount":89.4},{"date":"2022-07-29","category":"Uncategorized","amount":-4.22},{"date":"2022-07-17","category":"Uncategorized","amount":6.33},{"date":"2022-07-04","category":"Payment","amount":25},{"date":"2022-07-04","category":"Uncategorized","amount":5.4},{"date":"2022-07-02","category":"Travel","amount":-500},{"date":"2022-07-01","category":"Food and Drink","amount":12},{"date":"2022-07-01","category":"Food and Drink","amount":4.33},{"date":"2022-06-30","category":"Uncategorized","amount":89.4},{"date":"2022-06-29","category":"Uncategorized","amount":-4.22},{"date":"2022-06-17","category":"Uncategorized","amount":6.33},{"date":"2022-06-04","category":"Payment","amount":25},{"date":"2022-06-04","category":"Uncategorized","amount":5.4},{"date":"2022-06-02","category":"Travel","amount":-500},{"date":"2022-06-01","category":"Food and Drink","amount":12},{"date":"2022-06-01","category":"Food and Drink","amount":4.33},{"date":"2022-05-31","category":"Uncategorized","amount":89.4},{"date":"2022-05-30","category":"Uncategorized","amount":-4.22}]


def compute_smart_initial_budget(data):
    df = pd.read_json(data)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    expenses = df[df['amount'] < 0]
    income = df[df['amount'] > 0]
    monthly_expenses = expenses['amount'].resample('M').sum()
    monthly_income = income['amount'].resample('M').sum()
    monthly_expenses_df = monthly_expenses.reset_index()
    monthly_expenses_df.columns = ['Month', 'TotalExpenses']
    monthly_income_df = monthly_income.reset_index()
    monthly_income_df.columns = ['Month', 'TotalIncome']
    monthly_dashboard = pd.merge(
        monthly_income_df, monthly_expenses_df, on='Month', how='outer').fillna(0)
    monthly_dashboard['NetIncome'] = monthly_dashboard['TotalIncome'] + \
        monthly_dashboard['TotalExpenses']
    second_lowest_expense = monthly_expenses_df['TotalExpenses'].abs(
    ).sort_values().iloc[1]
    monthly_dashboard['PotentialIncome'] = monthly_dashboard['TotalIncome'] - \
        second_lowest_expense
    monthly_dashboard = monthly_dashboard.sort_values(
        by='Month').reset_index(drop=True)
    monthly_dashboard = monthly_dashboard[[
        'Month', 'TotalIncome', 'TotalExpenses', 'NetIncome', 'PotentialIncome']]
    accountBalance = monthly_dashboard['NetIncome'].sum()
    potentialBalance = monthly_dashboard['PotentialIncome'].sum()
    potentialSavings = potentialBalance - accountBalance
    potentialSavingsYearly = round(
        (potentialSavings / len(monthly_dashboard)) * 12, 2)
    specific_month = monthly_expenses_df.loc[monthly_expenses_df['TotalExpenses'].abs(
    ) == second_lowest_expense, 'Month'].values[0]
    specific_month = pd.Timestamp(specific_month)
    year = specific_month.year
    month = specific_month.month
    days_in_month = monthrange(year, month)[1]
    smart_budget = round(second_lowest_expense / days_in_month, 2)
    # return potentialSavingsYearly, smart_budget
    result = {
        "potentialSavingsYearly": potentialSavingsYearly,
        "smartBudget": smart_budget
    }

    print(json.dumps(result))
    return result


def ko(a, b):
    return a+b


if __name__ == "__main__":
    # data = sys.argv[1]
    data = sys.stdin.read()
    compute_smart_initial_budget(data)