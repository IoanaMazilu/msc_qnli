divided_amount_premise = 5887
divided_amount_hypothesis = 8887


# the hypothesis refers to the amount divided between Shyam and Ram mentioned in the premise
if divided_amount_premise >= divided_amount_hypothesis:
    # check if the amount in 'divided_amount_hypothesis' contradicts the amount divided in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
