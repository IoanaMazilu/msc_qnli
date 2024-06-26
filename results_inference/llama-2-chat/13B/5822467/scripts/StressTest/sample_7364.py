discount_premise = 30
listed_price_premise = 100
hypothesis_discount = 20
listed_price_hypothesis = 100

# the hypothesis refers to the discount on the listed price mentioned in the premise
if hypothesis_discount <= listed_price_premise * discount_premise / 100:
    # check if the estimate of 'listed_price_hypothesis' contradicts the discount on the listed price in the premise
    label = "contradiction"
elif listed_price_hypothesis!= listed_price_premise:
    # check if the listed price in the hypothesis contradicts the listed price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
