car_price_premise = 3
ac_price_premise = 2
car_price_hypothesis = 2
ac_price_hypothesis = 2

# the hypothesis refers to the ratio of the prices of a car and AC
if car_price_hypothesis <= car_price_premise and ac_price_hypothesis <= ac_price_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio of the prices of a car and AC
    # any ratio greater than 2:2 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
