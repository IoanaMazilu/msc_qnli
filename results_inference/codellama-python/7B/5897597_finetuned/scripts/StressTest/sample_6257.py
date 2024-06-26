discount_premise = 20
discount_hypothesis = 50
discount_value = 4

# the hypothesis refers to the discount percentage and the discount value mentioned in the premise
if discount_premise!= discount_hypothesis:
    # check if the discount percentage in the hypothesis contradicts the discount percentage in the premise
    label = "contradiction"
elif discount_value!= 4:
    # check if the discount value in the hypothesis contradicts the discount value in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
