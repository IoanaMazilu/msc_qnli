driving_rate_premise = 100
driving_rate_hypothesis = 400

# the hypothesis refers to the driving rate of Molly and Max mentioned in the premise
if driving_rate_premise >= driving_rate_hypothesis:
    # check if the estimate of 'driving_rate_hypothesis' contradicts the driving rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
