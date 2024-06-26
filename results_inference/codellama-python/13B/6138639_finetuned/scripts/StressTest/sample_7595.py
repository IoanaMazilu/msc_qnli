departure_time_premise = 60
departure_time_hypothesis = 70

# the hypothesis talks about the departure time of Dan from City A, referenced also in the premise
if departure_time_hypothesis!= departure_time_premise:
    # check if the departure time in the hypothesis contradicts the departure time reported in the premise
    label = "contradiction"
else:
    # if the departure time in the hypothesis does not contradict the departure time in the premise, we can infer entailment
    label = "entailment"

print(label)
