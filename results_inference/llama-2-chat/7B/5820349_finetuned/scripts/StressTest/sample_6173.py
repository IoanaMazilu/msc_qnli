john_tip_premise = 15
john_tip_hypothesis = 25

# the hypothesis refers to the tip percentage paid by John, which is also mentioned in the premise
if john_tip_premise!= john_tip_hypothesis:
    # check if the tip percentage in the hypothesis contradicts the tip percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
