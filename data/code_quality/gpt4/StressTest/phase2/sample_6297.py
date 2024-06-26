base_hours_premise = 12
base_hours_hypothesis = 82

# the hypothesis refers to the number of base hours worked by Harry, mentioned also in the premise
if base_hours_hypothesis >= base_hours_premise:
    # check if the number of 'base_hours_hypothesis' contradicts the number of base hours in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
