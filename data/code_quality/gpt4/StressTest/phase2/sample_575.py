ratio_premise = 10/5
ratio_hypothesis = 10/5

# The hypothesis refers to the ratio of distances between A to B and B to C mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # Check if the hypothesis's ratio contradicts the ratio in the premise
    label = "contradiction"
else:
    # The hypothesis doesn't contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
