price_car_premise = 3
price_ac_premise = 2
price_car_hypothesis = 2
price_ac_hypothesis = 2

# the hypothesis talks about a ratio between the price of a car and AC, which is also referred to in the premise
if price_car_hypothesis > price_car_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
elif price_ac_hypothesis > price_ac_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
