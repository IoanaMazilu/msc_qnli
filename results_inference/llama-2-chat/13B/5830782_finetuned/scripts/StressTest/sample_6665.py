chiefs_premise = 7
chiefs_hypothesis = 6

# the hypothesis talks about the number of Joint Chiefs of Staff at a meeting, referenced also in the premise
if chiefs_hypothesis!= chiefs_premise:
    # check if the number of chiefs in the hypothesis contradicts the number of chiefs reported in the premise
    label = "contradiction"
else:
    # if the number of chiefs in the hypothesis does not contradict the number of chiefs in the premise, we can infer entailment
    label = "entailment"

print(label)
