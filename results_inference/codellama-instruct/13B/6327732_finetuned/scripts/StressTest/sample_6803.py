bonds_purchased_premise = 50
bonds_purchased_hypothesis = 10

# the hypothesis refers to the denominations in which bonds are sold, but not the number of bonds purchased
if bonds_purchased_premise!= bonds_purchased_hypothesis:
    # check if the number of bonds purchased in the hypothesis contradicts the number of bonds purchased in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of bonds purchased
    # any number of bonds greater than 'bonds_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
