watermelons_premise = 136
watermelons_hypothesis = 536

# the hypothesis refers to the number of watermelons mike had after Sally left, which is also mentioned in the premise
if watermelons_premise >= watermelons_hypothesis:
    # check if the number of watermelons in the premise contradicts the estimate of less than 'watermelons_hypothesis'
    label = "contradiction"
else:
    # if the number of watermelons in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
