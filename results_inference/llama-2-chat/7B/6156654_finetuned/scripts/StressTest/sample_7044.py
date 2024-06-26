travel_time_premise = 10
travel_time_hypothesis = 20

# the hypothesis refers to the travel time of Raman, which is also mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif travel_time_hypothesis > travel_time_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise value, it is neutral
    label = "neutral"

print(label)
