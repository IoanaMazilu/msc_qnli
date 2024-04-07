# Premise: During a car trip, Maria stopped to rest after she traveled 1/2 of the total distance to her destination.
# Hypothesis: During a car trip, Maria stopped to rest after she traveled less than 8/2 of the total distance to her destination.
# Golden Label: entailment

travel_distance_premise = 1/2
travel_distance_hypothesis = 8/2

# The hypothesis refers to the distance Maria traveled before she stopped to rest, mentioned also in the premise
if travel_distance_hypothesis < travel_distance_premise:
    # Check if the hypothesis value contradicts the travel distance in the premise
    label = "contradiction"
elif travel_distance_hypothesis == travel_distance_premise:
    # If the hypothesis value equals the premise value, we can infer entailment
    label = "entailment"
else:
    # The premise gives only an exact fraction for the distance Maria traveled
    # A larger distance in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

