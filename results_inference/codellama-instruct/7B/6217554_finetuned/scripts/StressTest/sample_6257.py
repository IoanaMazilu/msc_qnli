discount_premise = 20
discount_hypothesis = 50

# the hypothesis talks about the discount percentage and the cost reduction for each person
if discount_hypothesis!= discount_premise:
    # check if the discount percentage in the hypothesis contradicts the discount percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
