distance_walked_premise = 7
distance_walked_hypothesis = 3
time_walked_premise = 1.25
time_walked_hypothesis = 1.25

# the hypothesis talks about the distance walked by Jack, referenced also in the premise
if distance_walked_hypothesis!= distance_walked_premise:
    # check if the distance walked in the hypothesis contradicts the distance walked in the premise
    label = "contradiction"
else:
    # the premise gives the time taken to walk the distance
    # the rate of walking in the hypothesis is the same as in the premise
    label = "entailment"

print(label)
