ylan (Hyderabad, Bangalore)

stations_premise = 18
stations_hypothesis = 48

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, which is also mentioned in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the number of stations in the premise
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"

print(label)
