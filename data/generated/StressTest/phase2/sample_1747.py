# Premise: Present ages of Sameer and Anand are in the ratio of more than 1:4 respectively.
# Hypothesis: Present ages of Sameer and Anand are in the ratio of 5:4 respectively.
# Golden Label: neutral

# The ratios are expressed as floats for accurate comparison
age_ratio_premise = 1/4
age_ratio_hypothesis = 5/4

# The hypothesis talks about the present age ratio of Sameer and Anand, referenced also in the premise
if age_ratio_hypothesis <= age_ratio_premise:
    # Check if the hypothesized ratio contradicts the ratio in the premise
    label = "contradiction"
elif age_ratio_hypothesis > age_ratio_premise:
    # The premise gives only an estimate for the ratio of ages
    # Any ratio of ages greater than 'age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

