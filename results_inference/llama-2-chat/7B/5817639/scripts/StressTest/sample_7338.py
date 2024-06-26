# Premise: If Sanoop returned 5 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
t_shirts_premise = 5

# Hypothesis: If Sanoop returned more than 4 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
t_shirts_hypothesis = 4

# calculate the difference between the number of t-shirts in the premise and the hypothesis
t_shirts_diff = t_shirts_hypothesis - t_shirts_premise

# check if the difference between the two values is positive
if t_shirts_diff > 0:
    # if the number of t-shirts in the hypothesis is greater than the number of t-shirts in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of t-shirts in the hypothesis is less than or equal to the number of t-shirts in the premise, we can infer contradiction
    label = "contradiction"

print(label)
