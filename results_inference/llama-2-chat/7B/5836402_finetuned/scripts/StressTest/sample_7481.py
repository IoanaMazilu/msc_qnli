dollars_per_hour_premise = 1
hours_worked_premise = 24
dollars_per_hour_hypothesis = 1
hours_worked_hypothesis = 54

# the hypothesis refers to the hours worked and the dollars per hour paid to Harry in a week, which are also mentioned in the premise
if hours_worked_hypothesis <= hours_worked_premise:
    # check if the hypothesis value contradicts the estimate of 'hours_worked_premise'
    label = "contradiction"
elif dollars_per_hour_hypothesis!= dollars_per_hour_premise:
    # check if the dollars per hour in the hypothesis contradicts the dollars per hour in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
