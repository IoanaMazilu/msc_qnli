car_price_premise = 3
ac_price_premise = 2
car_price_hypothesis = 8
ac_price_hypothesis = 2

# the hypothesis refers to the ratio of the prices of a car and AC
if car_price_hypothesis / ac_price_hypothesis!= car_price_premise / ac_price_premise:
    # check if the ratio of the prices in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives a ratio for the prices of a car and AC
    # any ratio of prices that is consistent with the premise is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
