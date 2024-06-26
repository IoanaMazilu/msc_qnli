discount_premise = 288
discount_hypothesis = 888

# the hypothesis talks about the discount on a sum, referenced also in the premise
if discount_hypothesis!= discount_premise:
    # check if the discount in the hypothesis contradicts the discount reported in the premise
    label = "contradiction"
else:
    # if the discount in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
