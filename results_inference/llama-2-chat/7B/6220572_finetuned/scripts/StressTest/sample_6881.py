bonds_purchased_premise = 1500
bonds_purchased_hypothesis = 7500

# the hypothesis refers to the number of purchased bonds mentioned in the premise
if bonds_purchased_hypothesis == bonds_purchased_premise:
    # check if the estimate of 'bonds_purchased_hypothesis' contradicts the number of purchased bonds in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purchased bonds
    # any number of purchased bonds consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
