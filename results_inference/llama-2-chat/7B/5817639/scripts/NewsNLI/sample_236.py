speed_premise = 0.8
speed_hypothesis = 0.8

# check if the hypothesis speed value contradicts the premise speed value
if speed_hypothesis!= speed_premise:
    label = "contradiction"
else:
    # if the hypothesis and premise speed values are the same, we can infer entailment
    label = "entailment"

print(label)
