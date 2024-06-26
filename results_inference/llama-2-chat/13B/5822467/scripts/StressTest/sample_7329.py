tower_premise = 4 * 3 * 1 = 12
tower_hypothesis = 3 * 3 * 1 + 1 = 11

# the hypothesis refers to the ratio of toy bricks used in the tower
if tower_hypothesis > tower_premise:
    # the hypothesis contradicts the premise, as it uses a different ratio
    label = "contradiction"
elif tower_hypothesis == tower_premise:
    # the hypothesis and premise have the same ratio, so there is no contradiction or entailment
    label = "neutral"
else:
    # the hypothesis uses a higher ratio than the premise, so we can entail the hypothesis from the premise
    label = "entailment"

print(label)
