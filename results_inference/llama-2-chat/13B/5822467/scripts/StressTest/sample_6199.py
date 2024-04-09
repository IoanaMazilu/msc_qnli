stations_premise = 48
stations_hypothesis = 18

# the hypothesis refers to the number of stations between Hyderabad and Bangalore, mentioned in the premise
if stations_premise > stations_hypothesis:
    # the hypothesis value contradicts the premise estimate
    label = "contradiction"
elif stations_hypothesis!= stations_premise:
    # the number of stations in the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis value is consistent with the premise estimate
    label = "entailment"

print(label)
