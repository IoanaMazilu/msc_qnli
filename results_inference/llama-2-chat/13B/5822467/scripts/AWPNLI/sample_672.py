customers_premise = 36.0
left_premise = 19.0
remaining_premise = 14.0
customers_hypothesis = 3.0

# compute the number of customers left after the first group left
left_customers_premise = left_premise + (remaining_premise - left_premise)

# compare the number of customers left in the premise to the number of customers in the hypothesis
if customers_hypothesis < left_customers_premise:
    # the hypothesis is contradictory to the premise, as there are more customers left in the premise than the number of customers in the hypothesis
    label = "contradiction"
elif customers_hypothesis > left_customers_premise:
    # the hypothesis is entailed by the premise, as there are fewer customers left in the premise than the number of customers in the hypothesis
    label = "entailment"
else:
    # the hypothesis and premise are neutral, as the number of customers left in the premise is the same as the number of customers in the hypothesis
    label = "neutral"

print(label)
