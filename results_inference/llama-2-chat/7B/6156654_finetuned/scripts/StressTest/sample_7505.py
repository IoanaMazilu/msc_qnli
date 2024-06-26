time_pat_stops_premise = 10
time_pat_stops_hypothesis = 60

# the hypothesis refers to the time Pat stops stretching, which is also mentioned in the premise
if time_pat_stops_hypothesis <= time_pat_stops_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif time_pat_stops_hypothesis > time_pat_stops_premise:
    # if the hypothesis value is greater than the premise value, it is a neutral case
    label = "neutral"
else:
    # if the hypothesis value is the same as the premise value, it is an entailment
    label = "entailment"

print(label)
