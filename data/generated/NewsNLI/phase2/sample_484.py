# Premise: But the investigation has already cost him at least one endorsement deal.
# Hypothesis: The investigation has already cost Hernandez at least one endorsement deal.
# Golden Label: entailment

endorsement_deals_lost_premise = 1
endorsement_deals_lost_hypothesis = 1

# the hypothesis mentions the loss of endorsement deals due to an investigation, which is also mentioned in the premise
# however, the hypothesis specifies Hernandez as the person affected, which cannot be entailed from the premise
label = "neutral"

print(label)

