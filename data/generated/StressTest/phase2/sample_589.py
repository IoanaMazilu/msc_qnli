# Premise: If the ratio between the one-third age of Neelam and half of Shaan's age of more than 4:9, then what is the school age of Shaan?
# Hypothesis: If the ratio between the one-third age of Neelam and half of Shaan's age of 5:9, then what is the school age of Shaan?
# Golden Label: neutral

ratio_premise = 4/9
ratio_hypothesis = 5/9

# the hypothesis refers to a ratio between the ages of Neelam and Shaan, which is also mentioned in the premise
if ratio_hypothesis != ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis doesn't contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

