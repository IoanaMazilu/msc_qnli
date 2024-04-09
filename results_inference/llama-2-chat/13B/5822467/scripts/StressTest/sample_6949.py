# define variables with representative names for the numerical entities in both inputs
age_ratio_premise = 1:4
age_ratio_hypothesis = 5:4

# extract all quantities as valid numbers (integers or floats)
age_premise = float(age_ratio_premise[0])
age_hypothesis = float(age_ratio_hypothesis[0])
age_diff_premise = age_hypothesis - age_premise

# use brief comments to explain what comparison we do between the defined variables
# the hypothesis ratio is 5:4, while the premise ratio is more than 1:4
# we can compare the two ratios to determine if the hypothesis contradicts, is neutral, or entails the premise

# check if the hypothesis ratio contradicts the premise ratio
if age_ratio_hypothesis[1]!= age_ratio_premise[1]:
    # the hypothesis ratio does not match the premise ratio, so we have a contradiction
    label = "contradiction"
elif age_diff_premise > 0:
    # the hypothesis ratio is closer to the premise ratio than the premise ratio is to the hypothesis ratio
    # we can infer entailment
    label = "entailment"
else:
    # the hypothesis ratio is further from the premise ratio than the premise ratio is from the hypothesis ratio
    # we have neutrality
    label = "neutral"

# print the comparison result
print(label)
