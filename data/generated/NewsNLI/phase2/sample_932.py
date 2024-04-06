# Premise: '' Widespread'' means that more than 50% of geographic regions in a state -- counties, for example -- are reporting flu activity.
# Hypothesis: All but two states are reporting widespread flu activity, according to CDC.
# Golden Label: neutral

widespread_premise = 0.50
widespread_hypothesis = None  # No specific quantity mentioned, but implies most states

# the hypothesis mentions widespread flu activity in almost all states, which aligns with the definition of "widespread" in the premise
# however, the hypothesis does not provide a specific percentage, and the premise does not provide information on the number of states reporting widespread flu activity

# As such, a direct comparison cannot be made and the label is neutral
label = "neutral"

print(label)

