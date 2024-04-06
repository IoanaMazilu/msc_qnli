# Premise: '' It was a hard one, to leave eight guys up there.''
# Hypothesis: Survivor says decision to leave eight behind was'' gut-wrenching''
# Golden Label: neutral

left_behind_premise = 8
left_behind_hypothesis = 8

# the hypothesis mentions the number of people left behind, which is also referenced in the premise
if left_behind_hypothesis != left_behind_premise:
    # check if the number of people left behind in the hypothesis contradicts the number of people left behind in the premise
    label = "contradiction"
else:
    # if the number of people left behind in the hypothesis does not contradict the number of people left behind in the premise, we can infer entailment
    label = "entailment"

print(label)

