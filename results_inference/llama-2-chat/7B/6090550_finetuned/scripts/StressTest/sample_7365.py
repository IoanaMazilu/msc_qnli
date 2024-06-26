# the rate of walking in the premise
rate_walking_premise = 7
# the rate of walking in the hypothesis
rate_walking_hypothesis = 2

# the hypothesis refers to a rate of walking greater than the rate in the premise
if rate_walking_hypothesis >= rate_walking_premise:
    # if the hypothesis rate is greater than the premise rate, then it's entailed by the premise
    label = "entailment"
else:
    # if the hypothesis rate is less than the premise rate, then it's contradicted by the premise
    label = "contradiction"

print(label)
