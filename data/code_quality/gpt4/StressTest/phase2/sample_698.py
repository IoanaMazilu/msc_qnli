old_ratio_premise = 5/3
old_ratio_hypothesis = 3/3

# the hypothesis refers to the age ratio in the future, mentioned in the premise
if old_ratio_premise != old_ratio_hypothesis:
    # check if the age ratio in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
else:
    label = "neutral"

print(label)
