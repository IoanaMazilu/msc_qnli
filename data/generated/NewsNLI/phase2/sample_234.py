# Premise: We know of only one way to fundamentally change our broken pay-to-play system:public funding of elections.
# Hypothesis: They say there's one way to fix our broken pay-to-play system:public funding of elections.
# Golden Label: entailment

ways_to_change_premise = 1
ways_to_change_hypothesis = 1

# the hypothesis mentions the number of ways to change the system, which is also mentioned in the premise
if ways_to_change_hypothesis != ways_to_change_premise:
    # check if the number of ways to change the system in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

