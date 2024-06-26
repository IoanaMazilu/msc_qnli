y_premise = 27
y_hypothesis = 47

# the hypothesis talks about the amount of butter mixed by Raman, referenced also in the premise
if y_hypothesis <= y_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"

print(label)
