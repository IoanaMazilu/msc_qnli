bail_premise = 5000000
bail_hypothesis = 1000000

# the hypothesis mentions a different bail amount than the premise
if bail_hypothesis!= bail_premise:
    # check if the bail amount in the hypothesis contradicts the bail amount in the premise
    label = "contradiction"
else:
    # if the hypothesis bail amount is the same as the premise bail amount, we can infer entailment
    label = "entailment"

print(label)
