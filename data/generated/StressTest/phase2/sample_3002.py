# Premise: At present, the ratio between the ages of Arun and Deepak is 4:3.
# Hypothesis: At present, the ratio between the ages of Arun and Deepak is less than 4:3.
# Golden Label: contradiction

arun_deepak_ratio_premise = 4 / 3
arun_deepak_ratio_hypothesis = 4 / 3

# The hypothesis refers to the age ratio of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_hypothesis >= arun_deepak_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

