children_premise = 4.0
pencils_per_child_premise = 2.0
total_pencils_hypothesis = 8.0

# compute the total number of pencils needed based on the premise
total_pencils_premise = children_premise * pencils_per_child_premise

if total_pencils_hypothesis > total_pencils_premise:
    # the hypothesis entails the premise
    label = "entailment"
elif total_pencils_hypothesis < total_pencils_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis and premise are neutral
    label = "neutral"

print(label)
