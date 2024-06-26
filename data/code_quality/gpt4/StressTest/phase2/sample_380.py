discount_premise = 20
discount_hypothesis = 30

# the hypothesis refers to the discount percentage on an item's original price mentioned in the premise
if discount_hypothesis != discount_premise:
    # check if the discount percentage in the hypothesis contradicts the discount percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
