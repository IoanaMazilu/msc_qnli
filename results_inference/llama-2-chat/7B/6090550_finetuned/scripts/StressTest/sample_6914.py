departure_rate_premise = 70
departure_rate_hypothesis = 50

# the hypothesis talks about the departure rate of flights from Phoenix, which is also mentioned in the premise
if departure_rate_hypothesis!= departure_rate_premise:
    # check if the departure rate in the hypothesis contradicts the departure rate in the premise
    label = "contradiction"
else:
    # if the departure rates are the same, we can infer entailment
    label = "entailment"

print(label)
