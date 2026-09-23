import pandas as pd

grades = pd.Series([4.5, 3.8, 4.9, 4.2], index=['Иванов', 'Петров', 'Сидоров', 'Козлов'])

print(grades)

mean_grade = grades.mean()
print(f'\nСредний балл по группе: {mean_grade:.2f}')

top_students = grades[grades > 4.0]
print('\nСтуденты с баллом выше 4.0:')
print(top_students)

data = {
    'Name': ['Анна', 'Борис', 'Виктор', 'Галина', 'Дмитрий'],
    'Age': [25, 32, 28, 35, 29],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'Salary': [60000, 50000, 75000, 80000, 52000],
    'Experience': [3, 8, 5, 12, 4]
}

df = pd.DataFrame(data)

print('\nТаблица сотрудников')
print(df)

print('\nОбщая информация o DataFrame')
df.info()

stats = df.describe()
print('\nОписательная статистика числовых колонок')
print(stats)

avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
print('\nСредняя зарплата по каждому отделу')
print(avg_salary_by_dept)

filtered_df = df[(df['Age'] > 28) & (df['Salary'] > 55000)]  
print('\nОтфильтрованный DataFrame по возрасту и зарплате')
print(filtered_df)

df['Salary_with_bonus'] = (df['Salary'] * 1.1).round(2)
print('\nDf с новым столбцом Salary_with_bonus')
print(df)

df_sorted = df.sort_values(by="Experience", ascending=False)
df_sorted = df_sorted.reset_index(drop=True)
print('\nОтсортированный DataFrame по убыванию стажа и сброшенными индексами')
print(df_sorted)

element_iloc = df_sorted.iloc[0, 2]
print(f'\nЭлемент 1-й строки и 3-го столбца (iloc): {element_iloc}')
element_loc = df_sorted.loc[1, 'Salary']
print(f'Зарплата сотрудника с индексом 1 (loc): {element_loc}')