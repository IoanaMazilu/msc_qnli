car_price_premise = 3
car_price_hypothesis = 8
ac_price_premise = 2
ac_price_hypothesis = 2

# the hypothesis refers to the ratio of car and AC prices mentioned in the premise
if car_price_premise * 2 == car_price_hypothesis:
    # check if the estimate of 'car_price_hypothesis' contradicts the ratio of car and AC prices in the premise
    label = "contradiction"
elif ac_price_hypothesis!= ac_price_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
