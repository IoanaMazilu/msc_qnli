toys_purchased_premise = 20
toys_per_dozen_premise = 375

toys_purchased_hypothesis = 20
toys_per_dozen_hypothesis = 675

# the hypothesis refers to the number of toys purchased and the rate per dozen, which are also mentioned in the premise
if toys_purchased_hypothesis!= toys_purchased_premise:
    # check if the number of toys purchased in the hypothesis contradicts the number of toys purchased in the premise
    label = "contradiction"
elif toys_per_dozen_hypothesis!= toys_per_dozen_premise:
    # check if the rate per dozen in the hypothesis contradicts the rate per dozen in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
