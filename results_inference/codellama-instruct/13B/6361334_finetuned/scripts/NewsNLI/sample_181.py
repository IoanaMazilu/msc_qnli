pledged_amount_premise = 90000000
pledged_amount_hypothesis = 90000000

# the hypothesis mentions the pledged amount of $90 million, which is also mentioned in the premise
if pledged_amount_hypothesis!= pledged_amount_premise:
    # check if the pledged amount in the hypothesis contradicts the pledged amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
