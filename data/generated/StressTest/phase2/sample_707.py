# Premise: By how much must Rebecca's annual income increase so that it constitutes 50% of Rebecca and Jimmy's combined income?
# Hypothesis: By how much must Rebecca's annual income increase so that it constitutes less than 50% of Rebecca and Jimmy's combined income?
# Golden Label: contradiction

percentage_premise = 50
percentage_hypothesis = 50

# The hypothesis talks about the percentage of Rebecca's annual income with respect to the combined income of Rebecca and Jimmy, which is also mentioned in the premise
if percentage_hypothesis >= percentage_premise:
    # Check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # The premise and hypothesis are talking about the same scenario but with different percentages
    # Any percentage less than 'percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

