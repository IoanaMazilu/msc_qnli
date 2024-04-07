# Premise: 6970, then what will be the share of Sameer in the profit?
# Hypothesis: more than 5970, then what will be the share of Sameer in the profit?
# Golden Label: entailment

sameer_share_premise = 6970
sameer_share_hypothesis = 5970

# the hypothesis refers to the share of Sameer mentioned in the premise
if sameer_share_hypothesis >= sameer_share_premise:
    # check if the hypothesis value contradicts the share of Sameer in the premise
    label = "contradiction"
elif sameer_share_hypothesis < sameer_share_premise:
    # check if the hypothesis value is less than the share of Sameer in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutral
    label = "neutral"

print(label)

