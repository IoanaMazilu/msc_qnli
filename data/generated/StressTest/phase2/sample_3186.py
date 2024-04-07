# Premise: At present, the ratio between the ages of Arun and Deepak is 4:3.
# Hypothesis: At present, the ratio between the ages of Arun and Deepak is less than 8:3.
# Golden Label: entailment

arun_to_deepak_premise = 4 / 3
arun_to_deepak_hypothesis = 8 / 3

# the hypothesis refers to the ratio between the ages of Arun and Deepak mentioned in the premise
if arun_to_deepak_hypothesis <= arun_to_deepak_premise:
    # check if the estimate of 'arun_to_deepak_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

