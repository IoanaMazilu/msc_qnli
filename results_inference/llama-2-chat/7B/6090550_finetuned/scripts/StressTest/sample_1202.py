y_premise = 7
y_hypothesis = 1

# the hypothesis talks about the same travel as the premise, but with different modes of transportation
if y_hypothesis!= y_premise:
    # check if the travel time in the hypothesis contradicts the travel time in the premise
    label = "contradiction"
else:
    # if the travel times match, we can infer entailment
    label = "entailment"

print(label)
