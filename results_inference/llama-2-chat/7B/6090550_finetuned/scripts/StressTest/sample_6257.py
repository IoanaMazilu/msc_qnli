discount_premise = 20
discount_hypothesis = 50
paid_each_premise = 4
paid_each_hypothesis = 4

# the hypothesis refers to the discount percentage and the paid amount each, both mentioned in the premise
if discount_hypothesis!= discount_premise:
    # check if the discount percentage in the hypothesis contradicts the discount percentage in the premise
    label = "contradiction"
elif paid_each_hypothesis!= paid_each_premise:
    # check if the paid amount each in the hypothesis contradicts the paid amount each in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
