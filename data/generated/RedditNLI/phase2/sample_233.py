# Premise: Amazon Hikes Monthly Prime Membership Prices by 18% to $12.99.
# Hypothesis: Amazon EBT membership $5.99 a month.
# Golden Label: neutral

price_increase_premise = 18
price_prime_premise = 12.99
price_ebt_hypothesis = 5.99

# the hypothesis introduces a new type of Amazon membership (EBT), which is not mentioned in the premise
# so, we can't establish a relationship between the two sentences based on the premise
label = "neutral"

print(label)

