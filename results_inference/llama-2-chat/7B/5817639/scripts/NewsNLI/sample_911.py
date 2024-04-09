win_premise = 0
lead_hypothesis = 0

# the premise mentions the possibility of Stenson winning the Race to Dubai, which is also referenced in the hypothesis
if lead_hypothesis!= win_premise:
    # check if the lead in the hypothesis contradicts the win reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
