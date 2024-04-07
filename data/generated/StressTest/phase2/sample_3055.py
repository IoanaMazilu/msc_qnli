# Premise: The ages of Patrick and Michael are in the ratio of more than 1:5 and that of Michael and Monica are in the ratio of 3:5.
# Hypothesis: The ages of Patrick and Michael are in the ratio of 3:5 and that of Michael and Monica are in the ratio of 3:5.
# Golden Label: neutral

# Define the ratios as two-element lists [numerator, denominator]
ratio_patrick_michael_premise = [1, 5]
ratio_michael_monica_premise = [3, 5]

ratio_patrick_michael_hypothesis = [3, 5]
ratio_michael_monica_hypothesis = [3, 5]

# Compare the ratios of the ages of Patrick to Michael and Michael to Monica
# in the premise and hypothesis

# The ratio of ages of Patrick to Michael in the hypothesis is greater than in the premise
if ratio_patrick_michael_hypothesis[0] / ratio_patrick_michael_hypothesis[1] <= ratio_patrick_michael_premise[0] / ratio_patrick_michael_premise[1]:
    label = "contradiction"
# The ratio of ages of Michael to Monica in the hypothesis is the same as in the premise
elif ratio_michael_monica_hypothesis != ratio_michael_monica_premise:
    label = "contradiction"
else:
    # If the ratios in the hypothesis do not contradict the ratios in the premise,
    # but the ratio of Patrick to Michael's ages is not directly inferable from the premise,
    # then the relationship is neutral
    label = "neutral"

print(label)

