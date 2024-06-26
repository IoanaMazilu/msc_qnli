oranges_premise = 50
oranges_hypothesis = 40

# the hypothesis refers to the average price of the pieces of fruit that Mary keeps
# the premise mentions the number of oranges that Mary must put back to achieve a certain average price
if oranges_hypothesis <= oranges_premise:
    # check if the hypothesis value contradicts the number of oranges in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of oranges
    # any number of oranges greater than 'oranges_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
