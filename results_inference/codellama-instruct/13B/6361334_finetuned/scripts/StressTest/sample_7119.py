price_car_premise = 3
price_ac_premise = 2
price_car_hypothesis = 2
price_ac_hypothesis = 2

# the hypothesis refers to the ratio of the price of a car and AC, which is also mentioned in the premise
if price_car_hypothesis <= price_car_premise and price_ac_hypothesis <= price_ac_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the price of a car and AC
    # any ratio greater than 'price_car_premise:price_ac_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
