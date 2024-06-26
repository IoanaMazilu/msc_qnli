time_premise = 6.01
time_hypothesis = 7.01

# the hypothesis talks about the time required by a train to cover the distance between Chennai and Jammu, referenced also in the premise
if time_hypothesis!= time_premise:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an exact time
    # the time in the hypothesis is the same as the time in the premise, so it can be explicitly entailed from the premise
    label = "entailment"

print(label)
