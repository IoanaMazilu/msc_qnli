# Premise: Most of those killed and hurt were young men, though four children were among the dead, police said.
# Hypothesis: Four of at least 27 people killed are children, police say.
# Golden Label: neutral

children_dead_premise = 4
children_dead_hypothesis = 4
total_dead_hypothesis = 27

# the hypothesis mentions the number of children among the dead, which is also referenced in the premise
# the hypothesis also provides a total number of people killed, which is not mentioned in the premise

if children_dead_hypothesis != children_dead_premise:
    # check if the number of children among the dead mentioned in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of children among the dead does not contradict the premise, we infer neutrality, because the total number of people killed is not mentioned in the premise
    label = "neutral"

print(label)

