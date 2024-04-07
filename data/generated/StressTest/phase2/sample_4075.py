# Premise: What was the difference between the total monthly salary of Arun in all the years together and Suman's monthly income in the year less than 6007?
# Hypothesis: What was the difference between the total monthly salary of Arun in all the years together and Suman's monthly income in the year 2007?
# Golden Label: neutral

salary_year_premise = 6007
salary_year_hypothesis = 2007

# the hypothesis asks about the difference in monthly salary between Arun and Suman in a specific year also mentioned in the premise
if salary_year_hypothesis >= salary_year_premise:
    # check if the year mentioned in the hypothesis contradicts the estimate of less than 'salary_year_premise' in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the year of Suman's salary
    # the exact year mentioned in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

