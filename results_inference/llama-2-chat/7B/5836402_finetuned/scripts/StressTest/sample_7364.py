discount_premise = 30
discount_hypothesis = 30

# the hypothesis refers to the discount percentage on the listed price mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the estimate of 'discount_hypothesis' contradicts the discount percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
