# Premise: Along with those killed, four French soldiers and three Afghan civilians were injured.
# Hypothesis: Five French soldiers, 1 Afghan civilian are killed.
# Golden Label: neutral

french_soldiers_injured_premise = 4
afghan_civilians_injured_premise = 3
french_soldiers_killed_hypothesis = 5
afghan_civilians_killed_hypothesis = 1

# the hypothesis mentions the number of French soldiers and Afghan civilians killed, which is different from the premise that refers to injured people
# so we need to check if the hypothesis contradicts the premise or is neutral

if french_soldiers_injured_premise == french_soldiers_killed_hypothesis and afghan_civilians_injured_premise == afghan_civilians_killed_hypothesis:
    # check if the number of French soldiers and Afghan civilians injured in the premise matches the number of them killed in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not match the premise values, we cannot infer entailment or contradiction, so the relation is neutral
    label = "neutral"

print(label)

