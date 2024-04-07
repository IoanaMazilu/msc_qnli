# Premise: He will be 5/3 times as old as Tom 6 years hence.
# Hypothesis: He will be more than 5/3 times as old as Tom 6 years hence.
# Golden Label: contradiction

age_ratio_premise = 5/3
age_ratio_hypothesis = 5/3

# the hypothesis refers to the age ratio between "he" and "Tom" 6 years hence, mentioned in the premise
if age_ratio_premise < age_ratio_hypothesis:
    # check if the 'age_ratio_hypothesis' contradicts the age ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

