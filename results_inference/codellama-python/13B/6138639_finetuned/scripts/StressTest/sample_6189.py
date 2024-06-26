days_to_save_premise = 30
days_to_save_hypothesis = 80
salary_per_day_premise = 125
salary_per_day_hypothesis = 125

# the hypothesis refers to the number of days Lexi needed to save and the salary per day, both mentioned in the premise
if days_to_save_hypothesis <= days_to_save_premise:
    # check if the estimate of 'days_to_save_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
elif salary_per_day_hypothesis!= salary_per_day_premise:
    # check if the salary per day in the hypothesis contradicts the salary per day reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
