# Premise: Investigators said the three arrested in Thailand are accused of directing the operation in Spain.
# Hypothesis: Two Pakistani men and a Thai woman are arrested in Thailand.
# Golden Label: neutral

arrested_premise = 3
arrested_hypothesis = 3

# the hypothesis mentions the number of people arrested in Thailand, which is also mentioned in the premise
# however, the hypothesis specifies the nationality of the arrested individuals, which cannot be entailed from the premise
label = "neutral"

print(label)

