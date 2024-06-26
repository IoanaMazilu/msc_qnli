y_premise = 15
y_hypothesis = 85

# the hypothesis talks about the distance between West-Town and East-Town, referenced also in the premise
if y_hypothesis!= y_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
