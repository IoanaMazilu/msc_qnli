age_ratio_premise = 5/3
age_ratio_hypothesis = 6/3

# the hypothesis refers to the age ratio of 'He' and 'Tom' in the future mentioned in the premise
if age_ratio_hypothesis >= age_ratio_premise:
    # check if the hypothesis ratio contradicts the age ratio in the premise
    label = "contradiction"
elif age_ratio_hypothesis <= age_ratio_premise:
    # check if the age ratio in the hypothesis is less than the age ratio in the premise
    label = "entailment"
else:
    # if none of the above conditions are met, the relation is neutral
    label = "neutral"

print(label)
