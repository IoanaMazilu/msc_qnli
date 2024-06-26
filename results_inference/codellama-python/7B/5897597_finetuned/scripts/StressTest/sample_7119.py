car_ac_ratio_premise = 3/2
car_ac_ratio_hypothesis = 2/2

# the hypothesis refers to the ratio of car and AC prices mentioned in the premise
if car_ac_ratio_premise <= car_ac_ratio_hypothesis:
    # check if the ratio of 'car_ac_ratio_hypothesis' contradicts the ratio of prices in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
