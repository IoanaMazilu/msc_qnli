original_price_premise = 100
discounted_price_premise = 85
tip_premise = 15

original_price_hypothesis = 100
discounted_price_hypothesis = 85
tip_hypothesis = 25

# the hypothesis refers to the tip paid over the original price of the dish, which is also mentioned in the premise
if tip_hypothesis <= tip_premise:
    # check if the estimate of 'tip_hypothesis' contradicts the tip paid in the premise
    label = "contradiction"
elif original_price_hypothesis!= original_price_premise:
    # check if the original price in the hypothesis contradicts the original price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)