car_ac_ratio_premise = 2
car_ac_ratio_hypothesis = 3/2

# the hypothesis refers to the ratio of the price of a car and AC mentioned in the premise
if car_ac_ratio_premise <= car_ac_ratio_hypothesis:
    # check if the estimate of 'car_ac_ratio_hypothesis' contradicts the ratio of the price of a car and AC in the premise
    label = "contradiction"
elif car_ac_ratio_hypothesis!= car_ac_ratio_premise:
    # check if the ratio of the price of a car and AC in the hypothesis contradicts the ratio of the price of a car and AC reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
