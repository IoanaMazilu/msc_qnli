miles_walked_premise = 4
miles_walked_hypothesis = 3
time_walked_premise = 1.25
time_walked_hypothesis = 1.25

# the hypothesis refers to the distance and time Jack walked, as stated in the premise
if miles_walked_hypothesis >= miles_walked_premise:
    # check if the hypothesis value contradicts the distance Jack walked in the premise
    label = "contradiction"
elif time_walked_hypothesis!= time_walked_premise:
    # check if the time Jack walked in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
