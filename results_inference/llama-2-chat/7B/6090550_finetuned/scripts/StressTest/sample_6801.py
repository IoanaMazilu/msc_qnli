# The hypothesis refers to the denominations of bonds sold, which is also mentioned in the premise
denomination_premise = 70
denomination_hypothesis = 70

# the hypothesis refers to the number of bonds purchased by Robert
bonds_purchased_hypothesis = 100

# the premise does not provide the number of bonds purchased
# we cannot infer the number of bonds purchased from the premise
bonds_purchased_premise = 100

# the hypothesis and premise have different values for the denominations of bonds sold
# we cannot infer entailment or contradiction based on the given information
label = "neutral"

print(label)
