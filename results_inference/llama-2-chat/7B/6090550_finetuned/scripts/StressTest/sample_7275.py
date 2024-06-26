y_premise = 100
y_hypothesis = 400

# the hypothesis talks about the driving rate of Molly and Max, referenced also in the premise
if y_premise >= y_hypothesis:
    # check if the driving rate in the premise contradicts the driving rate in the hypothesis
    label = "contradiction"
else:
    # if the driving rate in the premise is less than the driving rate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

