percentage_given_premise = 40
percentage_given_hypothesis = 60

# the hypothesis refers to the percentage of money Jones gave to his wife, which is also mentioned in the premise
if percentage_given_premise >= percentage_given_hypothesis:
    # check if the percentage in the premise contradicts the estimate of less than 'percentage_given_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
