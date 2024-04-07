# Premise: The price of a car and AC are in the ratio 3:2.
# Hypothesis: The price of a car and AC are in the ratio more than 2:2.
# Golden Label: entailment

car_ac_ratio_premise = 3 / 2
car_ac_ratio_hypothesis = 2 / 2

# the hypothesis refers to the ratio between the price of a car and AC mentioned in the premise
if car_ac_ratio_premise <= car_ac_ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the premise is larger than the one in the hypothesis, then the premise entails the hypothesis
    label = "entailment"

print(label)

