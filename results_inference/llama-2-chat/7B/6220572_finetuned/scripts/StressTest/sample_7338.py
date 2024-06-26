tshirts_returned_premise = 5
tshirts_returned_hypothesis = 4

# the hypothesis refers to the number of returned t-shirts and the average price of the remaining ones, both mentioned in the premise
if tshirts_returned_hypothesis <= tshirts_returned_premise:
    # check if the hypothesis value contradicts the number of returned t-shirts in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of returned t-shirts
    # any number of returned t-shirts greater than 'tshirts_returned_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
