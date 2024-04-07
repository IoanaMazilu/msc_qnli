# Premise: During a car trip, Maria stopped to rest after she traveled 1/2 of the total distance to her destination.
# Hypothesis: During a car trip, Maria stopped to rest after she traveled less than 1/2 of the total distance to her destination.
# Golden Label: contradiction

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

