customers_initial = 36.0
customers_left = 19.0
customers_remaining = 14.0
customers_hypothesis = 3.0

# the hypothesis refers to the number of customers the waiter had left to wait on
if customers_initial - customers_left!= customers_hypothesis:
    # check if the number of customers left does not match the hypothesis
    label = "contradiction"
else:
    # if the number of customers left matches the hypothesis, we can infer entailment
    label = "entailment"

print(label)
