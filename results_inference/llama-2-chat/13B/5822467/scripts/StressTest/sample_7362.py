discount_premise = 30
listed_price_premise = 100
hypothesis_discount = 10
listed_price_hypothesis = 100

# the hypothesis refers to the discount on the listed price, both mentioned in the premise
if hypothesis_discount > listed_price_premise * discount_premise / 100:
    # check if the estimate of the discount in the hypothesis contradicts the discount reported in the premise
    label = "contradiction"
elif listed_price_hypothesis!= listed_price_premise:
    # check if the listed price in the hypothesis contradicts the listed price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
