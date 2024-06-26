days_to_save_premise = 80
days_to_save_hypothesis = 30
daily_salary_premise = 125
daily_salary_hypothesis = 125

# the hypothesis refers to the number of days Lexi needs to save and the daily salary
if days_to_save_hypothesis >= days_to_save_premise:
    # check if the number of days in the hypothesis contradicts the estimate of less than 'days_to_save_premise'
    label = "contradiction"
elif daily_salary_hypothesis!= daily_salary_premise:
    # check if the daily salary in the hypothesis contradicts the daily salary reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
