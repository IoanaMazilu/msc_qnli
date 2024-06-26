car_price_ratio_premise = 3/2
car_price_ratio_hypothesis = 8/2

# the hypothesis refers to the ratio of car price to AC price mentioned in the premise
if car_price_ratio_premise!= car_price_ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
