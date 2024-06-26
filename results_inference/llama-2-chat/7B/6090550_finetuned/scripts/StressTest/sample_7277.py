y_premise = 100
y_hypothesis = 100

# the hypothesis talks about the driving rate of Molly and Max, which is also mentioned in the premise
if y_hypothesis >= y_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
