# Premise: If the ratio between the one-third age of Neelam and half of Shaan's age of 5:9, then what is the school age of Shaan?
# Hypothesis: If the ratio between the one-third age of Neelam and half of Shaan's age of less than 5:9, then what is the school age of Shaan?
# Golden Label: contradiction

# defining variables for numerical entities
ratio_premise = 5/9
ratio_hypothesis = 5/9

# the hypothesis talks about the ratio between the one-third age of Neelam and half of Shaan's age
if ratio_hypothesis > ratio_premise:
    # check if the hypothesis ratio contradicts the ratio in the premise
    label = "contradiction"
elif ratio_hypothesis == ratio_premise:
    # check if the hypothesis ratio can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # if the hypothesis ratio does not contradict the premise ratio and cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)

