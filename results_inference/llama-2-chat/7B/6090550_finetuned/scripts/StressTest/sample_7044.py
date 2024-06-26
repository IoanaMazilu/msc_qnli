y_premise = 10
y_hypothesis = 20

# the hypothesis talks about the number of hours Raman travelled, which is also mentioned in the premise
if y_hypothesis <= y_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"

print(label)
