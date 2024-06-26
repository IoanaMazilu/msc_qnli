ratio_premise_lewis = 1
ratio_premise_brown = 2
ratio_hypothesis_lewis = 8
ratio_hypothesis_brown = 2

# the hypothesis refers to the age ratio of Lewis and Brown mentioned in the premise
if ratio_hypothesis_lewis <= ratio_premise_lewis:
    # check if the 'ratio_hypothesis_lewis' contradicts the ratio of Lewis's age in the premise
    label = "contradiction"
elif ratio_hypothesis_brown != ratio_premise_brown:
    # check if the 'ratio_hypothesis_brown' contradicts the ratio of Brown's age in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we infer neutrality since less than 8:2 can include 1:2 but does not explicitly entail 1:2
    label = "neutral"

print(label)
