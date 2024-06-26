toys_premise = 20
toys_per_dozen_premise = 275

toys_hypothesis = 20
toys_per_dozen_hypothesis = 375

# the hypothesis talks about the number of toys and the rate per dozen, referenced also in the premise
if toys_hypothesis!= toys_premise:
    # check if the number of toys in the hypothesis contradicts the number of toys reported in the premise
    label = "contradiction"
elif toys_per_dozen_hypothesis!= toys_per_dozen_premise:
    # check if the rate per dozen in the hypothesis contradicts the rate per dozen in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
