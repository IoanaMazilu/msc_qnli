# Premise: The price of a car and AC are in the ratio 3:2.
# Hypothesis: The price of a car and AC are in the ratio 8:2.
# Golden Label: contradiction

car_ac_ratio_premise = 3/2
car_ac_ratio_hypothesis = 8/2

# the hypothesis is about the ratio between the price of a car and AC, which is also mentioned in the premise
if car_ac_ratio_hypothesis != car_ac_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis is the same as the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)

