time_travel_premise = 0.09
time_travel_hypothesis = 0.1

# the hypothesis mentions the percentage of people who would like to time travel, which is also mentioned in the premise
if time_travel_hypothesis!= time_travel_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
