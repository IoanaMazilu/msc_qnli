# Premise: 1300, Deepak's share is :
# Hypothesis: less than 1300, Deepak's share is :
# Golden Label: contradiction

share_premise = 1300
share_hypothesis = 1300

# the hypothesis refers to Deepak's share mentioned in the premise
if share_hypothesis >= share_premise:
    # check if the estimate of 'share_hypothesis' contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

