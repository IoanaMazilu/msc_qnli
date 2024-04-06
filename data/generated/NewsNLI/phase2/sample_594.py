# Premise: This growth was three times that of the overall UK hotel market.
# Hypothesis: Growth of budget hotels has been three times that of overall hotel market.
# Golden Label: neutral

growth_ratio_premise = 3
growth_ratio_hypothesis = 3

# the hypothesis mentions the growth ratio of some hotel aspect compared to the overall hotel market, which is also mentioned in the premise
# however, the hypothesis refers to budget hotels, which cannot be entailed from the premise
label = "neutral"

print(label)

