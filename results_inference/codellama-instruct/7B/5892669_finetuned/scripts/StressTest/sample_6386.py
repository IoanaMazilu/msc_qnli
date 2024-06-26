james_work_hours_premise = 45
james_work_hours_hypothesis = 35

# the hypothesis refers to the number of hours James worked, which is also mentioned in the premise
if james_work_hours_hypothesis!= james_work_hours_premise:
    # check if the number of hours James worked in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
