# Premise: Last year's collapse of Italian dairy company Parmalat, with '' 14.3 billion euros that must still be accounted for'', is given as evidence for '' a lack of effective tools and controls regarding financial operations''.
# Hypothesis: Parmalat costs 14.3 billion euros.
# Golden Label: neutral

unaccounted_funds_premise = 14.3e9
cost_hypothesis = 14.3e9

# the hypothesis talks about the cost of Parmalat which is not referenced in the premise (the premise talks about unaccounted funds)
# the hypothesis cannot be entailed from the premise, since the cost of Parmalat is unknown.
label = "neutral"

print(label)

