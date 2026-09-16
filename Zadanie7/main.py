import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(BASE_DIR, 'titanic.csv')
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'

def load_csv(url: str, out_path: str) -> pd.DataFrame:
    if not os.path.exists(output_path):
        print("Скачиваем файл с сервера...")
        df = pd.read_csv(url)
        df.to_csv(out_path, index=False)
        return df
    else:
        print("Файл найден на диске, загружаем из локальной папки...")
        df = pd.read_csv(out_path)
        return df

def main():
    
    df = load_csv(url=url, out_path=output_path)

    print(f'Размер датасета: {df.shape}')
    print('Первые 5 строк:')
    print(df.head())

    print('\n2. Информация о типах данных и непустых значениях:')
    df.info()

    missing_info = pd.DataFrame({
        'Пропуски': df.isnull().sum(),
        '% пропусков': (df.isnull().mean() * 100).round(2)
    })
    print(f'\n{missing_info[missing_info['Пропуски'] > 0]}')

    df = df.drop(columns=['Cabin'])
    print("\n4. Столбец 'Cabin' удален.")

    df['Age'] = df.groupby(['Sex', 'Pclass'])['Age'].transform(lambda x: x.fillna(x.median()))
    print("5. Пропуски в 'Age' заполнены медианным возрастом соответствующих подгрупп.")

    embarked_mode = df['Embarked'].mode()[0]
    df['Embarked'] = df['Embarked'].fillna(embarked_mode)
    print(f"6. Пропуски в 'Embarked' заполнены модой: '{embarked_mode}'.")

    remaining_nulls = df.isnull().sum().sum()
    print(f"7. Итоговое количество пропусков в датасете: {remaining_nulls}")

    duplicates_count = df.duplicated().sum()
    print(f"8. Найдено полных дубликатов строк: {duplicates_count}")
    if duplicates_count > 0:
        df = df.drop_duplicates()
        print("   Дубликаты удалены.")

    rename_mapping = {
        'Survived': 'Survival',
        'Pclass': 'Ticket_Class',
        'SibSp': 'Siblings_Spouse',
        'Parch': 'Parents_Children'
    }
    df = df.rename(columns=rename_mapping)
    print("\n9. Столбцы переименованы:")
    print(df.columns.tolist())

    output_file = os.path.join(BASE_DIR, 'titanic_cleaned.csv')
    df.to_csv(output_file, index=False)
    print(f"\n10. Очищенный датасет сохранен в файл '{output_file}'.")

if __name__ == '__main__':
    main()