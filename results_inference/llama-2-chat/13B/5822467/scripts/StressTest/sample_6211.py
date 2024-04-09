nhai_employees_premise = 600
nhai_employees_hypothesis = 100
highway_length_premise = 2000
highway_length_hypothesis = 2000
days_premise = 50
days_hypothesis = 50
hours_per_day_premise = 8
hours_per_day_hypothesis = 8

# the hypothesis talks about the number of employees and the length of the highway, referenced also in the premise
if nhai_employees_hypothesis <= nhai_employees_premise:
    # check if the hypothesis value contradicts the estimate of less than 'nhai_employees_premise'
    label = "contradiction"
elif highway_length_hypothesis!= highway_length_premise:
    # check if the length of the highway in the hypothesis contradicts the length reported in the premise
    label = "contradiction"
elif days_hypothesis!= days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif hours_per_day_hypothesis!= hours_per_day_premise:
    # check if the number of hours per day in the hypothesis contradicts the number of hours per day reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
