departure_rate_premise = 50
departure_rate_hypothesis = 40

# the hypothesis talks about the on-time departure rate, referenced also in the premise
if departure_rate_hypothesis >= departure_rate_premise:
    # check if the hypothesis value contradicts the estimate of higher than 'departure_rate_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
