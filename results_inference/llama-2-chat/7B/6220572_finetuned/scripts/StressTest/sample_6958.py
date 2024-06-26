toys_purchased_premise = 20
toys_purchased_hypothesis = 20
rate_per_dozen_premise = 275
rate_per_dozen_hypothesis = 375

# the hypothesis talks about the number of toys purchased and the rate per dozen, also referenced in the premise
if toys_purchased_hypothesis!= toys_purchased_premise:
    # check if the number of toys purchased in the hypothesis contradicts the number of toys purchased in the premise
    label = "contradiction"
elif rate_per_dozen_hypothesis!= rate_per_dozen_premise:
    # check if the rate per dozen in the hypothesis contradicts the rate per dozen reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
