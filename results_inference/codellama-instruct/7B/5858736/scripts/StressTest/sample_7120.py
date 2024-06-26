car_price_premise = 2
car_price_hypothesis = 3
ac_price_premise = 2
ac_price_hypothesis = 2

# the hypothesis talks about the ratio of the prices of a car and AC
if car_price_hypothesis / ac_price_hypothesis <= car_price_premise / ac_price_premise:
    # check if the ratio of the prices in the hypothesis contradicts the ratio of the prices in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the prices
    # any ratio greater than 'car_price_premise / ac_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
