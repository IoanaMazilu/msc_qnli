money_given_premise = 40
money_given_hypothesis = 70

# the hypothesis refers to the percentage of money Jones gave to his wife, which is also mentioned in the premise
if money_given_premise >= money_given_hypothesis:
    # check if the percentage of money given in the premise contradicts the estimate of less than'money_given_hypothesis'
    label = "contradiction"
else:
    # if the percentage of money given in the premise is less than'money_given_hypothesis', we can infer entailment
    label = "entailment"

print(label)
