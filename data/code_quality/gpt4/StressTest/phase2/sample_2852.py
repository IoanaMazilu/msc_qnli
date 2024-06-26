regular_hours_premise = 40
regular_hours_hypothesis = 70

# the hypothesis refers to the hourly rate and the number of regular hours worked per week as mentioned in the premise
if regular_hours_hypothesis != regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
