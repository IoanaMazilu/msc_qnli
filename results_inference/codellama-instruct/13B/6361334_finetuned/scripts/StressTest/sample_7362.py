discount_premise = 30
discount_hypothesis = 10

# the hypothesis refers to the discount percentage mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the estimate of 'discount_hypothesis' contradicts the discount percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
