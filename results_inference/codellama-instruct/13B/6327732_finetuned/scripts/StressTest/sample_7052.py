premise_share = 1300
hypothesis_share = 1300

# the hypothesis refers to the number of shares mentioned in the premise
if hypothesis_share >= premise_share:
    # check if the estimate of 'hypothesis_share' contradicts the number of shares in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
