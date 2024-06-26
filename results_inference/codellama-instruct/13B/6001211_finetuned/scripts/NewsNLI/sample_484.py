endorsement_deals_premise = 1
endorsement_deals_hypothesis = 1

# the hypothesis mentions the number of endorsement deals lost due to the investigation, which is also mentioned in the premise
if endorsement_deals_hypothesis!= endorsement_deals_premise:
    # check if the number of endorsement deals lost in the hypothesis contradicts the number of deals lost in the premise
    label = "contradiction"
else:
    # if the number of endorsement deals lost in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
