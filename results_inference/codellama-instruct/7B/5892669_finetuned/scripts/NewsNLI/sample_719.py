facebook_purchase_premise = 1000000000
facebook_purchase_hypothesis = 1000000000

# the hypothesis mentions the price Facebook paid for Instagram, which is also mentioned in the premise
if facebook_purchase_hypothesis!= facebook_purchase_premise:
    # check if the price in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
