# Premise: At present, the ratio between the ages of Arun and Deepak is 4:5.
# Hypothesis: At present, the ratio between the ages of Arun and Deepak is less than 4:5.
# Golden Label: contradiction

arun_deepak_ratio_premise = 4/5
arun_deepak_ratio_hypothesis = 4/5

# the hypothesis refers to the age ratio of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_premise < arun_deepak_ratio_hypothesis:
    # check if the ratio in 'arun_deepak_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif arun_deepak_ratio_premise > arun_deepak_ratio_hypothesis:
    # check if the ratio in 'arun_deepak_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

