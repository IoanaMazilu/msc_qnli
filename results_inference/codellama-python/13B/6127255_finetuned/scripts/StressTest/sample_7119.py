car_ac_ratio_premise = 3/2
car_ac_ratio_hypothesis = 2/2

# the hypothesis refers to the ratio of the price of a car and AC mentioned in the premise
if car_ac_ratio_premise <= car_ac_ratio_hypothesis:
    # check if the estimate of 'car_ac_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
