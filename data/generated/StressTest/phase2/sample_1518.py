# Premise: 2000, Deepak's share is :
# Hypothesis: less than 4000, Deepak's share is :
# Golden Label: entailment

deepak_share_premise = 2000
deepak_share_hypothesis = 4000

# the hypothesis refers to the amount of Deepak's share mentioned in the premise
if deepak_share_hypothesis <= deepak_share_premise:
    # check if the estimate of 'deepak_share_hypothesis' contradicts the value of Deepak's share in the premise
    label = "contradiction"
elif deepak_share_premise != deepak_share_hypothesis:
    # check if the value of Deepak's share in the hypothesis contradicts the value of Deepak's share reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

