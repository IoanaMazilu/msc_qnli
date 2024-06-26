y_premise = 80
y_hypothesis = 30

# the hypothesis talks about the percentile of Lena's grade, referenced also in the premise
if y_hypothesis <= y_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise value is greater than the hypothesis value, we can infer entailment
    label = "entailment"

print(label)
