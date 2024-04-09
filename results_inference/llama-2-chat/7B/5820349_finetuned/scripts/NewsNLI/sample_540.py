concerned_premise = 1/3
not_worried_premise = 69
worried_hypothesis = 52

# the hypothesis mentions the percentage of Americans worried about a bridge collapse, which is also referenced in the premise
# however, the hypothesis provides a different percentage than the premise
if worried_hypothesis!= concerned_premise:
    # check if the percentage of worried Americans in the hypothesis contradicts the percentage of worried Americans in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
