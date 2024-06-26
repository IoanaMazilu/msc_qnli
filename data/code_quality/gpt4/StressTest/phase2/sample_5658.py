travel_distance_premise = 1/2
travel_distance_hypothesis = 5/2

# the hypothesis talks about the distance Maria traveled during a trip, referenced also in the premise
if travel_distance_hypothesis < travel_distance_premise:
    # check if the hypothesis value contradicts the distance traveled by Maria reported in the premise
    label = "contradiction"
elif travel_distance_hypothesis == travel_distance_premise:
    # check if the hypothesis value is exactly the same as the premise's
    label = "entailment"
else:
    # the premise specifies that Maria traveled 1/2 of the total distance
    # any distance less than 5/2 but more than 1/2 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
