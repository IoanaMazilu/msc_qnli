regular_hours_premise = 24
regular_hours_hypothesis = 84

# the hypothesis refers to the number of regular hours Harry is paid x dollars per hour, which is also mentioned in the premise
if regular_hours_hypothesis < regular_hours_premise:
    # check if the hypothesis value contradicts the number of regular hours in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
