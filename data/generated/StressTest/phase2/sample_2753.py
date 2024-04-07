# Premise: If the ratio of their ages is 7:9, how old is Sandy?
# Hypothesis: If the ratio of their ages is 4:9, how old is Sandy?
# Golden Label: contradiction

age_ratio_premise = 7/9
age_ratio_hypothesis = 4/9

# the hypothesis refers to the age ratio mentioned in the premise
if age_ratio_premise != age_ratio_hypothesis:
    # check if the age ratio in the hypothesis contradicts the age ratio mentioned in the premise
    label = "contradiction"
else:
    # if the age ratio in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

