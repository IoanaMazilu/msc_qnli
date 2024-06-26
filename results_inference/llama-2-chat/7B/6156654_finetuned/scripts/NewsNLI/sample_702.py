# the percentage of people who think of the United States as an enemy is more than 69%
positive_view_percentage_premise = 12
contradiction_premise = positive_view_percentage_premise < 69

# the hypothesis refers to the same percentage as the premise
hypothesis_contradiction_premise = 69

# check if the hypothesis percentage contradicts the premise percentage
if contradiction_premise:
    label = "contradiction"
elif positive_view_percentage_premise > hypothesis_contradiction_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
