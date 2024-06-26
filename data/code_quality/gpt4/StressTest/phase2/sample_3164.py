distance_travelled_premise = 0.5
distance_travelled_hypothesis = 0.5

# the hypothesis refers to the distance travelled in the premise
if distance_travelled_hypothesis >= distance_travelled_premise:
    # check if the hypothesis value contradicts the information in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the one in the premise, it is entailed by the premise
    label = "entailment"

print(label)
