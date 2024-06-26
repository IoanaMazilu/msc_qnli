travel_time_premise = 7 * 24 * 60 + 1  # time in minutes
travel_time_hypothesis = 6 * 24 * 60 + 1  # time in minutes

# the hypothesis talks about the travel time between two cities, referenced also in the premise
if travel_time_hypothesis >= travel_time_premise:
    # check if the hypothesis value contradicts the exact time of 'travel_time_premise'
    label = "contradiction"
elif travel_time_hypothesis < travel_time_premise:
    # if the hypothesis value is less than the premise value, it's consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is exactly the same as the premise value, we can infer entailment
    label = "entailment"

print(label)
