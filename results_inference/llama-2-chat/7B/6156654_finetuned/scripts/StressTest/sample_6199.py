stations_premise = 48
stations_hypothesis = 18

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, which is also mentioned in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif stations_hypothesis < stations_premise:
    # if the hypothesis value is less than the premise, it is consistent with the premise
    # but we cannot infer entailment since the premise does not provide a specific upper bound for the number of stations
    label = "neutral"
else:
    # if the hypothesis value is exactly equal to the premise, we can infer entailment
    label = "entailment"

print(label)
