
# PyCity Schools Analysis

* As a whole, schools with higher budgets, did not yield better test results. By contrast, schools with higher spending per student actually (\$645-675) underperformed compared to schools with smaller budgets (<\$585 per student).

* As a whole, smaller and medium sized schools dramatically out-performed large sized schools on passing math performances (89-91% passing vs 67%).

* As a whole, charter schools out-performed the public district schools across all metrics. However, more analysis will be required to glean if the effect is due to school practices or the fact that charter schools tend to serve smaller student populations per school. 
---

### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

# Display merged table. 
school_data_complete.head()

## District Summary

* Calculate the total number of schools

* Calculate the total number of students

* Calculate the total budget

* Calculate the average math score 

* Calculate the average reading score

* Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2

* Calculate the percentage of students with a passing math score (70 or greater)

* Calculate the percentage of students with a passing reading score (70 or greater)

* Create a dataframe to hold the above results

* Optional: give the displayed data cleaner formatting

# District Summary 

# Calculations for district summary
schools_calc = school_data_complete['school_name'].value_counts()
schools_total = schools_calc.count()

# Calculate number of students
students_total = len(school_data_complete['student_name']) 

# Calculate the budget by school using mean. Budget of school same for all of the same school so mean would return same value. 
budget_calc = school_data_complete.groupby('school_name')['budget'].mean()
budget_total = budget_calc.sum()

# Calculate average math score & reading score
avg_math = school_data_complete['math_score'].mean()
avg_reading = school_data_complete['reading_score'].mean()

# Calculate overall passing by taking average of above two calculations
overall_passing = (avg_math + avg_reading)/ 2

# Calculating the percent passing each subject. 
passing_math = school_data_complete[school_data_complete['math_score'] >= 70].count()/ students_total
percent_passing_math = passing_math['math_score']*100

passing_reading = school_data_complete[school_data_complete['reading_score'] > 70].count()/ students_total
percent_passing_reading = passing_reading['reading_score']*100

# Create new DataFrame with calculations for district summary.
district_summary_df = pd.DataFrame({
    "Total Schools":[schools_total],
    "Total Students":[students_total],
    "Total Budget":[budget_total],
    "Average Math Score": [avg_math],
    "Average Reading Score":[avg_reading],
    "% Passing Math":[percent_passing_math],
    "% Passing Reading":[percent_passing_reading],
    "% Overall Passing Rate":[overall_passing]                                                
})

district_summary_df



## School Summary

* Create an overview table that summarizes key metrics about each school, including:
  * School Name
  * School Type
  * Total Students
  * Total School Budget
  * Per Student Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)
  
* Create a dataframe to hold the above results

# Create school summary

school_summary_ss = school_data_complete[['school_name', 'type', 'budget', 'math_score', 'reading_score', 'size']]

school_type_ss = school_summary_ss.groupby('school_name')['type'].unique()

#Calculations for average size
students_total_ss = school_summary_ss.groupby('school_name')['size'].mean()

#Calculations for budget
budget_total_ss = school_summary_ss.groupby('school_name')['budget'].mean()

#Calculations for budget per student
budget_student_ss = budget_total_ss/ students_total_ss

#Calculations for math score by school
avg_math_ss = school_summary_ss.groupby('school_name')['math_score'].mean()

#Calculations for reading score by school
avg_reading_ss = school_summary_ss.groupby('school_name')['reading_score'].mean()

#Caclculations for percent passing math by school
percent_math_ss = school_summary_ss[school_summary_ss['math_score'] >= 70].groupby('school_name')['math_score'].count()/students_total_ss *100

#Caclculations for percent passing reading by school
percent_reading_ss = school_summary_ss[school_summary_ss['reading_score'] >= 70].groupby('school_name')['reading_score'].count()/students_total_ss * 100

#Calculation for overall passing both math and reading
overall_passing_ss = (percent_math_ss + percent_reading_ss)/2

# New DataFrame
school_summary_ss_df = pd.DataFrame({
    "School Type": school_type_ss,
    "Total Students": students_total_ss,
    "Total School Budget": budget_total_ss,
    "Per Student Budget": budget_student_ss,
    "Average Math Score": avg_math_ss,
    "Average Reading Score": avg_reading_ss,
    "% Passing Math": percent_math_ss,
    "% Passing Reading": percent_reading_ss,
    "Overall Passing Rate": overall_passing_ss
})

school_summary_ss_df

## Top Performing Schools (By Passing Rate)

* Sort and display the top five schools in overall passing rate

# Sort by top 5 schools overall passing rate

top_5_overall = school_summary_ss_df.sort_values('Overall Passing Rate', ascending = False)

top_5_overall.head()



## Bottom Performing Schools (By Passing Rate)

* Sort and display the five worst-performing schools

# Sort by bottom 5 schools overall passing rate

bot_5_overall = school_summary_ss_df.sort_values('Overall Passing Rate', ascending = True)

bot_5_overall.head()



## Math Scores by Grade

* Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

  * Create a pandas series for each grade. Hint: use a conditional statement.
  
  * Group each series by school
  
  * Combine the series into a dataframe
  
  * Optional: give the displayed data cleaner formatting

# Display schools with unique name

school_list = school_data_complete['school_name'].unique()
school_list

# Math Scores by Grade

math_scores_by_grade = school_data_complete[['school_name', 'grade', 'math_score']]

# Calculations for each grades score using groupby for school name and then averaging the math score.
ninth_grade_math = math_scores_by_grade.loc[math_scores_by_grade['grade'] == '9th'].groupby('school_name')['math_score'].mean()
tenth_grade_math = math_scores_by_grade.loc[math_scores_by_grade['grade'] == '10th'].groupby('school_name')['math_score'].mean()
elevin_grade_math = math_scores_by_grade.loc[math_scores_by_grade['grade'] == '11th'].groupby('school_name')['math_score'].mean()
twelve_grade_math = math_scores_by_grade.loc[math_scores_by_grade['grade'] == '12th'].groupby('school_name')['math_score'].mean()


# Create new DataFrame.
math_grades = pd.DataFrame({
    "9th": ninth_grade_math,
    "10th": tenth_grade_math,
    "11th": elevin_grade_math,
    "12th": twelve_grade_math
})

math_grades



## Reading Score by Grade 

* Perform the same operations as above for reading scores

# Reading Scores by Grade.
# Used same logic as Math except directed towards Reading column.

reading_scores_by_grade = school_data_complete[['school_name', 'grade', 'reading_score']]

ninth_grade_read = reading_scores_by_grade.loc[reading_scores_by_grade['grade'] == '9th'].groupby('school_name')['reading_score'].mean()
tenth_grade_read = reading_scores_by_grade.loc[reading_scores_by_grade['grade'] == '10th'].groupby('school_name')['reading_score'].mean()
elevin_grade_read = reading_scores_by_grade.loc[reading_scores_by_grade['grade'] == '11th'].groupby('school_name')['reading_score'].mean()
twelve_grade_read = reading_scores_by_grade.loc[reading_scores_by_grade['grade'] == '12th'].groupby('school_name')['reading_score'].mean()


read_grades = pd.DataFrame({
    "9th": ninth_grade_read,
    "10th": tenth_grade_read,
    "11th": elevin_grade_read,
    "12th": twelve_grade_read
})

read_grades



## Scores by School Spending

* Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)

# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-685"]

# Scores by School Spending

# Used below to determine my max and min
#print((budget_total_ss/ students_total_ss).max()) # Idenitfy max at 655
#print((budget_total_ss/ students_total_ss).min()) # Identify min at 578

# Creation of bins
budget_bins = [0, 585, 615, 645, 685]
group_names_spend = ["<$585", "$585-615", "$615-645", "$645-685"]

# calculate the budget per student
budget_calculation = school_data_complete['budget']/school_data_complete['size'] 

# add column with budget calculation to end of data frame
school_data_complete['budget_calculation'] = budget_calculation.values 

# Place the data series into a new column inside of DataFrame
pd.cut(school_data_complete['budget_calculation'], budget_bins, labels = group_names_spend)

school_data_complete['Spend_Group'] = pd.cut(school_data_complete['budget_calculation'], budget_bins, labels = group_names_spend)

# Create a Groupby object based on Spend Group
scores_by_school_spend = school_data_complete.groupby('Spend_Group')


# Calculations for average math scores, reading scores, and percent passing each subject
avg_math_sbs = scores_by_school_spend['math_score'].mean()

avg_reading_sbs = scores_by_school_spend['reading_score'].mean()

percent_math_sbs = school_data_complete[school_data_complete['math_score'] >= 70].groupby('Spend_Group')['math_score'].count()/scores_by_school_spend['math_score'].count() * 100 

percent_reading_sbs = school_data_complete[school_data_complete['reading_score'] >= 70].groupby('Spend_Group')['reading_score'].count()/scores_by_school_spend['reading_score'].count() * 100

overall_passing_sbs = (percent_math_sbs + percent_reading_sbs)/2


# Create new DataFrame
school_summary_by_spend_df = pd.DataFrame({
    "Average Math Score": avg_math_sbs,
    "Average Reading Score": avg_reading_sbs,
    "% Passing Math": percent_math_sbs,
    "% Passing Reading": percent_reading_sbs,
    "Overall Passing Rate": overall_passing_sbs
})


school_summary_by_spend_df



## Scores by School Size

* Perform the same operations as above, based on school size.

# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

# scores by School Size
# Used same logic as for School Spending except adjusted for School Size

size_bins = [0, 1000, 3000, 6000]
group_names_size = ["Small (<1000)", "Medium (1000-3000)", "Large (3000-6000)"]

school_data_complete['School Size'] = pd.cut(school_data_complete['size'], size_bins, labels = group_names_size)

scores_by_school_size = school_data_complete.groupby('School Size')


# Calculations
avg_math_sss = scores_by_school_size['math_score'].mean()

avg_reading_sss = scores_by_school_size['reading_score'].mean()

percent_math_sss = school_data_complete[school_data_complete['math_score'] >= 70].groupby('School Size')['math_score'].count()/scores_by_school_size['math_score'].count() * 100 

percent_reading_sss = school_data_complete[school_data_complete['reading_score'] >= 70].groupby('School Size')['reading_score'].count()/scores_by_school_size['reading_score'].count() * 100

overall_passing_sss = (percent_math_sss + percent_reading_sss)/2

# New DataFrame
school_summary_by_size_df = pd.DataFrame({
    "Average Math Score": avg_math_sss,
    "Average Reading Score": avg_reading_sss,
    "% Passing Math": percent_math_sss,
    "% Passing Reading": percent_reading_sss,
    "Overall Passing Rate": overall_passing_sss
})


school_summary_by_size_df



## Scores by School Type

* Perform the same operations as above, based on school type.

# scores by School Type
# Used same logic as for School Spending except adjusted for School Type

scores_by_school_type = school_data_complete.groupby('type')

# Calculations
avg_math_sst = scores_by_school_type['math_score'].mean()

avg_reading_sst = scores_by_school_type['reading_score'].mean()

percent_math_sst = school_data_complete[school_data_complete['math_score'] >= 70].groupby('type')['math_score'].count()/scores_by_school_type['math_score'].count() * 100 

percent_reading_sst = school_data_complete[school_data_complete['reading_score'] >= 70].groupby('type')['reading_score'].count()/scores_by_school_type['reading_score'].count() * 100

overall_passing_sst = (percent_math_sst + percent_reading_sst)/2

# Create new DataFrame
school_summary_by_type_df = pd.DataFrame({
    "Average Math Score": avg_math_sst,
    "Average Reading Score": avg_reading_sst,
    "% Passing Math": percent_math_sst,
    "% Passing Reading": percent_reading_sst,
    "Overall Passing Rate": overall_passing_sst
})


school_summary_by_type_df



# Observable Trends

# 1) One trend that is interesting is across all 15 schools, all schools have higher average reading scores and higher 
        # reading pass rates than math scores. Knowing this I would want to further explore how surrounding areas compare
        # to see if we are laggin behind in math. If so, it may lead to allocating more budget money to math programs. 
        
# 2) When looking at Charter vs District schools, Charter schools perfromed significantly better, however, their budget
        # per student was on average lower than the budget per student for District schools. One area that I would want to
        # explore more would be the student to teacher ratio. On average District schools have more than 2,000 students 
        # where as the Charter schools are generally under 2,000 students. 

# 3) An initial assumption I had was the higher the budget per student the higher the passing rates. However, after seeing 
        # the results it is the opposite. The schools with lower budgets performed better than schools with higher budgets
        # per students. A combination of this observation and observation # 2 would next want me to explore teacher to student
        # ratios. 