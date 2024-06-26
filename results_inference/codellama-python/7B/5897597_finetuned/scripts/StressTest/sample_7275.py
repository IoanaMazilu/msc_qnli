driving_rate_premise = 100
driving_rate_hypothesis = 400

# the hypothesis refers to the driving rate mentioned in the premise
if driving_rate_premise >= driving_rate_hypothesis:
    # check if the driving rate in the premise contradicts the estimate of less than 'driving_rate_hypothesis'
    label = "contradiction"
else:
    # if the driving rate in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
