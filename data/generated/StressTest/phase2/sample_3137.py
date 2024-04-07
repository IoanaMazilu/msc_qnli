# Premise: 2000, Deepak's share is :
# Hypothesis: 8000, Deepak's share is :
# Golden Label: contradiction

deepak_share_premise = 2000
deepak_share_hypothesis = 8000

# the hypothesis refers to the Deepak's share mentioned in the premise
if deepak_share_hypothesis != deepak_share_premise:
    # check if the value of Deepak's share in the hypothesis contradicts the value of Deepak's share in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

