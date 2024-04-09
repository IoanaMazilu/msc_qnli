price_car_premise = 2
price_ac_premise = 2
price_car_hypothesis = 3
price_ac_hypothesis = 2

# the hypothesis talks about the ratio of the price of a car and AC, referenced also in the premise
if price_car_hypothesis / price_car_premise > 1:
    # check if the ratio of the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif price_ac_hypothesis / price_ac_premise > 1:
    # check if the ratio of the AC in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio of the hypothesis values and estimates do not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
