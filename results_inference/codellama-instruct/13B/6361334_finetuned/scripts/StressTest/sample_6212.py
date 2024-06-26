employees_premise = 100
employees_hypothesis = 200
days_premise = 50
days_hypothesis = 50
km_premise = 2
km_hypothesis = 2
hours_premise = 8
hours_hypothesis = 8

# the hypothesis refers to the number of employees and the length of the highway mentioned in the premise
if employees_hypothesis <= employees_premise:
    # check if the estimate of 'employees_hypothesis' contradicts the number of employees in the premise
    label = "contradiction"
elif km_hypothesis!= km_premise:
    # check if the length of the highway in the hypothesis contradicts the length of the highway reported in the premise
    label = "contradiction"
elif days_hypothesis!= days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif hours_hypothesis!= hours_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
