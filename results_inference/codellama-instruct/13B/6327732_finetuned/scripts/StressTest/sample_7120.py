car_price_premise = 2
ac_price_premise = 2
car_price_hypothesis = 3
ac_price_hypothesis = 2

# the hypothesis refers to the ratio of the price of a car and AC
if car_price_hypothesis / ac_price_hypothesis!= car_price_premise / ac_price_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the price of a car and AC
    # any ratio greater than 'car_price_premise / ac_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
