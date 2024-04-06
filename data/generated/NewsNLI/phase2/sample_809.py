# Premise: The billionaire real estate mogul is suing millionaire comedian Bill Maher for $5 million.
# Hypothesis: The comedian offers $5 million for Trump to prove otherwise.
# Golden Label: neutral

suing_amount_premise = 5000000
offer_amount_hypothesis = 5000000

# the hypothesis mentions the amount offered by the comedian, which is also referenced in the premise
# however, the context of the amount's usage cannot be entailed from the premise
label = "neutral"

print(label)

