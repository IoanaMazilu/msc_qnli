# Premise: During a car trip, Maria stopped to rest after she traveled 1/2 of the total distance to her destination.
# Hypothesis: During a car trip, Maria stopped to rest after she traveled 7/2 of the total distance to her destination.
# Golden Label: contradiction

distance_travelled_premise = 1/2
distance_travelled_hypothesis = 7/2

# the hypothesis refers to the distance travelled by Maria during her car trip, which is also mentioned in the premise
if distance_travelled_hypothesis == distance_travelled_premise:
    # check if the hypothesis value is the same as the premise value
    label = "entailment"
elif distance_travelled_hypothesis < distance_travelled_premise:
    # check if the hypothesis value contradicts the premise by being less than it
    label = "contradiction"
else:
    # if the hypothesis value is not the same as nor less than the premise, it is a neutral case
    label = "neutral"

print(label)

