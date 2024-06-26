distance_premise = 500
distance_hypothesis = 700
speed_both = 18

# both the premise and hypothesis refer to the time Sandy needs to cover specific distances running at a certain speed
if distance_hypothesis != distance_premise:
    # the distance in the hypothesis is different from the one in the premise
    label = "contradiction"
else:
    # if the distances were the same, the time to cover would be the same, leading to entailment
    label = "entailment"

print(label)
