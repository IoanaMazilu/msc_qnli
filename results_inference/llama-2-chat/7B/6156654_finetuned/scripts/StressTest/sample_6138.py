travel_time_premise = 7
travel_time_hypothesis = 4

# the hypothesis refers to the travel time from A to B and back, which is also mentioned in the premise
if travel_time_hypothesis < travel_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif travel_time_hypothesis == travel_time_premise:
    # if the hypothesis value equals the premise value, it's a neutral case
    label = "neutral"
else:
    # if the hypothesis value is greater than the premise value, it's an entailment
    label = "entailment"

print(label)
