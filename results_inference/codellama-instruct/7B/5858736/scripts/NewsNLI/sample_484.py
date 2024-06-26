endorsement_deal_premise = 1
endorsement_deal_hypothesis = 1

# the hypothesis mentions the number of endorsement deals that the investigation has cost Hernandez, which is also mentioned in the premise
if endorsement_deal_hypothesis!= endorsement_deal_premise:
    # check if the number of endorsement deals from the hypothesis contradicts the number of endorsement deals mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
