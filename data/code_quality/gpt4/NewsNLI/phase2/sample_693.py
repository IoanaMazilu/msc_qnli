active_psychiatrists_premise = 50
active_psychiatrists_hypothesis = 50

# the hypothesis mentions the number of active psychiatrists in the country, which is also mentioned in the premise
if active_psychiatrists_hypothesis != active_psychiatrists_premise:
    # check if the number of active psychiatrists in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
