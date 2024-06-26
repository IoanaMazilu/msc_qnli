ride_time_premise = 1
ride_time_hypothesis = 3

# the hypothesis talks about the duration of the bike ride, which is also mentioned in the premise
if ride_time_hypothesis <= ride_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif ride_time_hypothesis > ride_time_premise:
    # check if the hypothesis value is more than the premise value
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
