departure_diff_premise = 120
departure_diff_hypothesis = 120

# the hypothesis refers to the time difference between Dan's and Cara's departures mentioned in the premise
if departure_diff_premise > departure_diff_hypothesis:
    # check if the estimate of 'departure_diff_hypothesis' contradicts the departure time difference in the premise
    label = "contradiction"
elif departure_diff_premise < departure_diff_hypothesis:
    # check if the departure time difference in the hypothesis contradicts the departure time difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
