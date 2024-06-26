car_ac_ratio_premise = 2 / 2
car_ac_ratio_hypothesis = 3 / 2

# The hypothesis refers to the ratio of the price of a car to the price of an AC, also mentioned in the premise
if car_ac_ratio_hypothesis <= car_ac_ratio_premise:
    # Check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the ratio
    # Any ratio greater than 'car_ac_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
