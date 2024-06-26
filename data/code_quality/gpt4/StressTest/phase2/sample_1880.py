travel_time_premise = 11
travel_time_hypothesis = 11

# The hypothesis talks about Pavan's travel time, which is also mentioned in the premise
if travel_time_hypothesis >= travel_time_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # If the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
