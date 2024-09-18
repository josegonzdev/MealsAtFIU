import json
import pandas as pd


with open('dinner_data.json') as file:
    data = json.load(file)

# normalize the JSON data to extract food items and nutrients
df = pd.json_normalize(
    data, 
    record_path=['menu', 'periods', 'categories', 'items', 'nutrients'], 
    meta=[
        ['menu', 'periods', 'categories', 'items', 'name'],  # Food item name
        ['menu', 'periods', 'categories', 'items', 'portion'],  # Portion size
    ],
    errors='ignore'
)

# pivot dataFrame into different columns/rows/etc (Calories, Protein, Carbs, etc.)
df_pivot = df.pivot_table(
    index=['menu.periods.categories.items.name', 'menu.periods.categories.items.portion'],  # Use food name and portion as index
    columns='name',  # Use the nutrient name (Calories, Protein, etc.) as columns
    values='value_numeric',  # The numeric value of the nutrient
    aggfunc='first'
).reset_index()

# print the results to console
print(df_pivot.head())

# saves to a CSV
df_pivot.to_csv('dinner_table.csv', index=False)


