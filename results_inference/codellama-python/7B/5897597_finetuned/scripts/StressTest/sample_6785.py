base_hours_premise = 40
base_hours_hypothesis = 40

# the hypothesis refers to the number of hours James is paid x dollars per hour, as mentioned in the premise
if base_hours_hypothesis <= base_hours_premise:
    # check if the hypothesis value contradicts the number of base hours in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
