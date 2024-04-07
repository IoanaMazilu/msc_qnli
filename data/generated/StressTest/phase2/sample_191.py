# Premise: If the ratio between the one-third age of Neelam and half of Shaan's age of 5:9, then what is the school age of Shaan?
# Hypothesis: If the ratio between the one-third age of Neelam and half of Shaan's age of 8:9, then what is the school age of Shaan?
# Golden Label: contradiction

shaan_age_premise = 5
ratio_premise = 5/9
shaan_age_hypothesis = 1
ratio_hypothesis = 8/9

# the hypothesis talks about the ratio between Neelam's and Shaan's ages, referenced also in the premise
if shaan_age_hypothesis != shaan_age_premise:
    # check if the value of 'shaan_age_hypothesis' contradicts 'shaan_age_premise'
    label = "contradiction"
elif ratio_hypothesis != ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

