employees_premise = 600
employees_hypothesis = 100
days_premise = 50
days_hypothesis = 50
hours_premise = 8
hours_hypothesis = 8
distance_premise = 2
distance_hypothesis = 2

# the hypothesis refers to the number of employees and the distance of the highway mentioned in the premise
if employees_hypothesis <= employees_premise:
    # check if the estimate of 'employees_hypothesis' contradicts the number of employees in the premise
    label = "contradiction"
elif distance_hypothesis!= distance_premise:
    # check if the distance of the highway in the hypothesis contradicts the distance of the highway reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
