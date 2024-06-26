# defining the age ratio for Roonie and Ronaldo as per premise and hypothesis
age_ratio_roonie_ronaldo_premise = 7/7
age_ratio_roonie_ronaldo_hypothesis = 6/7

# the hypothesis refers to the age ratio of Roonie and Ronaldo one year ago mentioned in the premise
if age_ratio_roonie_ronaldo_hypothesis > age_ratio_roonie_ronaldo_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
elif age_ratio_roonie_ronaldo_hypothesis == age_ratio_roonie_ronaldo_premise:
    # check if the age ratio in the hypothesis is equal to the age ratio in the premise
    label = "contradiction"
else:
    # if the age ratio in the hypothesis is less than the age ratio in the premise
    # then it is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
