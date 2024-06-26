saved_salary_percentage_premise = 50
saved_salary_percentage_hypothesis = 10

# the hypothesis talks about the percentage of salary saved by Kishore, referenced also in the premise
if saved_salary_percentage_hypothesis >= saved_salary_percentage_premise:
    # check if the hypothesis value contradicts the estimate of less than 'saved_salary_percentage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of saved salary
    # any percentage of saved salary less than 'saved_salary_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
