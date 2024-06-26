working_hours_premise = 10
working_hours_hypothesis = 70

# the hypothesis refers to the number of working hours mentioned in the premise
if working_hours_hypothesis!= working_hours_premise:
    # check if the number of working hours in the hypothesis contradicts the number of working hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)