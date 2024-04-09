hourly_wage_premise = 100
hourly_wage_hypothesis = 80

# the hypothesis refers to the number of hours worked per week, which is also mentioned in the premise
if hourly_wage_hypothesis <= hourly_wage_premise:
    # check if the hypothesis value contradicts the estimate of 'hourly_wage_premise'
    label = "contradiction"
elif hourly_wage_hypothesis > 84:
    # check if the number of hours worked in the hypothesis contradicts the number of hours worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
