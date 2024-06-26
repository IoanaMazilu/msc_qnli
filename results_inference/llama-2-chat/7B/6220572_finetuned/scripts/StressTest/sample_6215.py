employees_premise = 10
employees_hypothesis = 70
working_hours_premise = 10
working_hours_hypothesis = 70

# the hypothesis refers to the number of working hours and the number of employees needed to finish a task, both mentioned in the premise
if employees_hypothesis <= employees_premise:
    # check if the estimate of 'employees_hypothesis' contradicts the number of employees in the premise
    label = "contradiction"
elif working_hours_hypothesis!= working_hours_premise:
    # check if the number of working hours in the hypothesis contradicts the number of working hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
