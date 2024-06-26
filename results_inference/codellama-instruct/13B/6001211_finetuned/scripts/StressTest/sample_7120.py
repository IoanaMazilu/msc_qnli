car_ac_ratio_premise = 2
car_ac_ratio_hypothesis = 3/2

# the hypothesis refers to the ratio of prices of a car and AC mentioned in the premise
if car_ac_ratio_hypothesis <= car_ac_ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimate of more than 'car_ac_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of prices
    # any ratio greater than 'car_ac_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
