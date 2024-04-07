# Premise: By how much must Rebecca's annual income increase so that it constitutes less than 60% of Rebecca and Jimmy's combined income?
# Hypothesis: By how much must Rebecca's annual income increase so that it constitutes 50% of Rebecca and Jimmy's combined income?
# Golden Label: neutral

percentage_premise = 60
percentage_hypothesis = 50

# Both the premise and the hypothesis are talking about the percentage of Rebecca's income in relation to the combined income of Rebecca and Jimmy.
if percentage_hypothesis >= percentage_premise:
    # If the percentage in the hypothesis is greater than or equal to the percentage in the premise, it contradicts the premise.
    label = "contradiction"
elif percentage_hypothesis < percentage_premise:
    # If the percentage in the hypothesis is less than the percentage in the premise, it does not contradict the premise. However, it cannot be explicitly entailed from the premise.
    label = "neutral"

print(label)

