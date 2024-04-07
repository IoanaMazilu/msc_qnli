# Premise: At present, the ratio between the ages of Arun and Deepak is 4:3.
# Hypothesis: At present, the ratio between the ages of Arun and Deepak is 2:3.
# Golden Label: contradiction

arun_deepak_ratio_premise = 4/3
arun_deepak_ratio_hypothesis = 2/3

# the hypothesis talks about the age ratio of Arun and Deepak, which is also mentioned in the premise
if arun_deepak_ratio_hypothesis == arun_deepak_ratio_premise:
    # check if the ratio in the hypothesis matches the ratio in the premise
    label = "entailment"
else:
    # if the ratio in the hypothesis does not match with the ratio in the premise, it is a contradiction
    label = "contradiction"

print(label)

