endorsement_deals_lost_premise = 1
endorsement_deals_lost_hypothesis = 1

# the hypothesis mentions the number of endorsement deals lost due to the investigation, which is also referenced in the premise
if endorsement_deals_lost_hypothesis!= endorsement_deals_lost_premise:
    # check if the number of endorsement deals lost in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
