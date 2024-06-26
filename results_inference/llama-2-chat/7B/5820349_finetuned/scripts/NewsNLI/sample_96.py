time_travel_interest_premise = 0.09
time_travel_interest_hypothesis = 0.1

# the hypothesis mentions the percentage of people interested in time travel, which is also referenced in the premise
if time_travel_interest_hypothesis!= time_travel_interest_premise:
    # check if the time travel interest in the hypothesis contradicts the time travel interest reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
