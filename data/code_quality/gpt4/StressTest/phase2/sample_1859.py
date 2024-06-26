sugar_premise = 12
oil_premise = 3
sugar_hypothesis = 12
oil_hypothesis = 3

# the hypothesis talks about the quantity of sugar and oil in Laura's cookie recipe, referenced also in the premise
if sugar_hypothesis <= sugar_premise:
    # check if the hypothesis value contradicts the estimate of more than 'sugar_hypothesis'
    label = "contradiction"
else:
    # the premise gives the exact number of sugar required for each 3 g of oil
    # any number of sugar greater than 'sugar_premise' contradicts the premise
    label = "neutral"

print(label)
