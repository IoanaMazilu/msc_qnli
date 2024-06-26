price_car_premise = 3
price_ac_premise = 2
price_car_hypothesis = 8
price_ac_hypothesis = 2

# the hypothesis talks about the ratio of the price of a car and AC, which is also mentioned in the premise
if price_car_hypothesis / price_car_premise == price_ac_hypothesis / price_ac_premise:
    # check if the ratio of the hypothesis matches the ratio in the premise
    label = "entailment"
elif price_ac_hypothesis < price_ac_premise:
    # check if the ratio of the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio,
    # any ratio consistent with the premise is neutral, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
