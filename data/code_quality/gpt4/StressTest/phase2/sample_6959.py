toys_purchased_premise = 20
toys_purchased_hypothesis = 20
rate_per_dozen_premise = 375
rate_per_dozen_hypothesis = 675

# the hypothesis refers to the number of toys purchased and the rate per dozen
if toys_purchased_premise != toys_purchased_hypothesis:
    # check if the number of sold toys in the hypothesis contradicts the number of toys purchased in the premise
    label = "contradiction"
elif rate_per_dozen_premise != rate_per_dozen_hypothesis:
    # check if the rate per dozen in the hypothesis contradicts the rate per dozen in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
