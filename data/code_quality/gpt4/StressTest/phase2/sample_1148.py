males_premise = 25
males_hypothesis = 15

# the hypothesis talks about the number of males, referenced also in the premise
if males_hypothesis != males_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
