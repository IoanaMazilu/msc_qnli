distance_travelled_premise = 1/2
distance_travelled_hypothesis = 5/2

# the hypothesis refers to the distance travelled by Maria, mentioned also in the premise
if distance_travelled_hypothesis != distance_travelled_premise:
    # check if the distance travelled in the hypothesis contradicts the distance travelled reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value is the same as the premise one, we can infer entailment
    label = "entailment"

print(label)
