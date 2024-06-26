regular_hours_premise = 40
regular_hours_hypothesis = 60

# the hypothesis refers to the number of regular hours paid at x dollars per hour, mentioned in the premise
if regular_hours_hypothesis <= regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
