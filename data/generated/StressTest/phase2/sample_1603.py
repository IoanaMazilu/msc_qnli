# Premise: By how much must Rebecca's annual income increase so that it constitutes more than 15% of Rebecca and Jimmy's combined income?
# Hypothesis: By how much must Rebecca's annual income increase so that it constitutes 55% of Rebecca and Jimmy's combined income?
# Golden Label: neutral

# The premise and hypothesis are about percentages of Rebecca's income increase over the combined income of Rebecca and Jimmy
percentage_increase_premise = 15
percentage_increase_hypothesis = 55

# Now we compare those percentages
# If they are equal, then the hypothesis fully and explicitly entailed from the premise
if percentage_increase_premise == percentage_increase_hypothesis:
    label = "entailment"
# If they are not equal, then the hypothesis cannot be fully and explicitly entailed from the premise
# But it is also not contradicting the premise, as the premise doesn't specify an upper limit to the percentage increase
else:
    label = "neutral"

print(label)

