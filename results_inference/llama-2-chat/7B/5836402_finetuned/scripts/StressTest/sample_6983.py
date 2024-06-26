rate_premise = 6
rate_hypothesis = 8

# the hypothesis refers to the interest rate at which Nitin borrowed money, which is also mentioned in the premise
if rate_hypothesis!= rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
