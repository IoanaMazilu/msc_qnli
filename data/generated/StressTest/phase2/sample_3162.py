# Premise: During a car trip, Maria stopped to rest after she traveled 1/2 of the total distance to her destination.
# Hypothesis: During a car trip, Maria stopped to rest after she traveled less than 3/2 of the total distance to her destination.
# Golden Label: entailment

distance_traveled_premise = 1/2
distance_traveled_hypothesis = 3/2

# the hypothesis refers to the distance traveled by Maria during her trip, also mentioned in the premise
if distance_traveled_hypothesis < distance_traveled_premise:
    # check if the hypothesis value contradicts the distance traveled by Maria in the premise
    label = "contradiction"
elif distance_traveled_hypothesis == distance_traveled_premise:
    # if the distance traveled by Maria in the hypothesis equals the distance in the premise, we can infer entailment
    label = "entailment"
else:
    # any distance less than 3/2 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

