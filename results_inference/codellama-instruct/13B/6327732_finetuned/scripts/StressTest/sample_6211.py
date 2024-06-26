nhai_employees_premise = 600
nhai_employees_hypothesis = 100
highway_length_premise = 2
highway_length_hypothesis = 2
work_days_premise = 50
work_days_hypothesis = 50
work_hours_premise = 8
work_hours_hypothesis = 8

# the hypothesis refers to the number of employees and the length of the highway mentioned in the premise
if nhai_employees_hypothesis <= nhai_employees_premise:
    # check if the estimate of 'nhai_employees_hypothesis' contradicts the number of employees in the premise
    label = "contradiction"
elif highway_length_hypothesis!= highway_length_premise:
    # check if the length of the highway in the hypothesis contradicts the length of the highway reported in the premise
    label = "contradiction"
elif work_days_hypothesis!= work_days_premise:
    # check if the number of work days in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
elif work_hours_hypothesis!= work_hours_premise:
    # check if the number of work hours in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)