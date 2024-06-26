sales_offer_premise = 20
sales_offer_hypothesis = 80

# the hypothesis refers to the discount percentage for shirts, mentioned in the premise
if sales_offer_hypothesis!= sales_offer_premise:
    # check if the discount percentage in the hypothesis contradicts the discount percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
