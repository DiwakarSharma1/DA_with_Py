import pandas as pd

def calculate_demographic_data(print_data=True):
# Read data from file
    df = pd.read_csv('adult.data.csv')
    
# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

# What is the average age of men?
    average_age_men = round(df.loc[df['sex']=='Male', 'age'].mean(),1)

# What is the percentage of people who have a Bachelor's degree?
    total_people=df.shape[0]
    total_bachelors=(df['education']=='Bachelors').sum()
    percentage_bachelors = round((total_bachelors/total_people)*100,1)

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
# What percentage of people without advanced education make more than 50K?

# with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = (df['education'].isin(['Bachelors','Masters','Doctorate'])).sum()
    lower_education = (~df['education'].isin(['Bachelors','Masters','Doctorate'])).sum()

    higher_education_r = ((df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary']=='>50K')).sum()
    lower_education_r = ((~df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary']=='>50K')).sum()

# percentage with salary >50K
    higher_education_rich = round((higher_education_r/higher_education)*100,1)
    lower_education_rich = round((lower_education_r/lower_education)*100,1)

# What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (df['hours-per-week']==df['hours-per-week'].min()).sum()
    num_min_workers_rich = ((df['hours-per-week']==df['hours-per-week'].min()) & (df['salary']=='>50K')).sum()
    rich_percentage = round((num_min_workers_rich/num_min_workers)*100 , 1)


    # Count total people per country
    country_people = df['native-country'].value_counts()
    # Count rich people per country
    country_people_rich = df.loc[df['salary'] == '>50K', 'native-country'].value_counts()
    # Build a DataFrame
    dfc = pd.DataFrame({
        'country_people': country_people,
        'country_people_rich': country_people_rich
    })
    # Fill missing values with 0 (for countries with no >50K earners)
    dfc = dfc.fillna(0)
    # Calculate percentage
    dfc['country_rich_percentage'] = round((dfc['country_people_rich'] / dfc['country_people']) * 100, 1)

# What country has the highest percentage of people that earn >50K?
    highest_earning_country = dfc['country_rich_percentage'].idxmax()
    highest_earning_country_percentage = dfc['country_rich_percentage'].max()

# Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[((df['salary']=='>50K')&(df['native-country']=='India')) ,'occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
