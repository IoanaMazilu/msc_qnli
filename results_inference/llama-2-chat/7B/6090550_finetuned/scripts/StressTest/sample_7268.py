y_premise = 600
y_hypothesis = 500

# the hypothesis talks about the length of the circular track that Bruce and Bhishma are running on
# the hypothesis refers to a length that is different from the one mentioned in the premise

if y_hypothesis!= y_premise:
    # check if the length of the track in the hypothesis contradicts the length of the track in the premise
    label = "contradiction"
else:
    # if the length of the track in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
