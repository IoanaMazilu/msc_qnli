# Premise: It was a remarkable finish to a remarkable game and it left Portugal and Denmark locked together on three points each after two Group B games.
# Hypothesis: Portugal seal 3-2 win over Denmark in Group B.
# Golden Label: neutral

points_portugal_premise = 3
points_denmark_premise = 3
points_portugal_hypothesis = 3
points_denmark_hypothesis = 2

# the hypothesis mentions the points of Portugal and Denmark in Group B, which are also referenced in the premise
# however, the hypothesis implies that Portugal won over Denmark, which cannot be entailed from the premise
label = "neutral"

print(label)
