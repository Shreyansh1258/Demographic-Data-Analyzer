import pandas as pd

def calculate_demographic_data(print_data=True):
    # CSV
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race',
        'sex', 'capital-gain', 'capital-loss', 'hours-per-week',
        'native-country', 'salary'
    ]
    df = pd.read_csv("adult_data.csv", names=column_names, skipinitialspace=True)
    
    
    numeric_cols = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    #now calculations begin 
    race_count = df['race'].value_counts()
    avg_age = df[df['sex']== "Male"]['age'].mean().round(1)
    
    num_bachelors = len(df[df['education'] == "Bachelors"])
    total = len(df)
    pct_bach = round((num_bachelors/total)*100,1)
    
    higher_df = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_df = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    
    higher = len(higher_df[higher_df['salary'] == ">50K"])
    lower = len(lower_df[lower_df['salary'] == ">50K"])
    
    high_edu_rich = round(higher / len(higher_df) * 100, 1)
    low_edu_rich = round(lower / len(lower_df) * 100, 1)
    
    min_hrs = df['hours-per-week'].min()
    num_min_hrs = df[df['hours-per-week']==min_hrs]
    percent_min_hrs_rich = round((num_min_hrs['salary']==">50K").mean()*100,1)
    
    country_earnings = df[df['salary']==">50K"]['native-country'].value_counts()
    total_country = df['native-country'].value_counts()
    
    if not country_earnings.empty:
        country_percent = (country_earnings / total_country * 100)
        highest_earning_country = country_percent.idxmax()
        highest_earning_country_pct = round(country_percent.max(), 1)
    else:
        highest_earning_country = None
        highest_earning_country_pct = 0
    
    people_in = df[(df['native-country']=="India") & (df['salary']==">50K")]
    ocupat = people_in['occupation'].value_counts()
    if not ocupat.empty:
        top_in_edu = ocupat.idxmax()
    else:
        top_in_edu = None
    
    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", avg_age)
        print("Percentage with Bachelors:", pct_bach)
        print("Higher education rich %:", high_edu_rich)
        print("Lower education rich %:", low_edu_rich)
        print("Min work hours:", min_hrs)
        print("Rich % among min workers:", percent_min_hrs_rich)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country %:", highest_earning_country_pct)
        print("Top occupation in India:", top_in_edu)
    
    return {
        'race_count': race_count,
        'average_age_men': avg_age,
        'percentage_bachelors': pct_bach,
        'higher_education_rich': high_edu_rich,
        'lower_education_rich': low_edu_rich,
        'min_work_hours': min_hrs,
        'rich_percentage': percent_min_hrs_rich,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_pct,
        'top_IN_occupation': top_in_edu
    }