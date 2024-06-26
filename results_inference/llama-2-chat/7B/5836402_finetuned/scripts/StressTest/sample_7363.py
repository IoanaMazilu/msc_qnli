discount_premise = 10
discount_hypothesis = 30

# the hypothesis refers to the discount on the listed price of a calculator, mentioned in the premise
if discount_hypothesis > discount_premise:
    # check if the estimate of 'discount_hypothesis' contradicts the discount mentioned in the premise
    label = "contradiction"
elif discount_hypothesis < discount_premise:
    # check if the discount in the hypothesis contradicts the discount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
