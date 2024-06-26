wheat_purchased_premise = 30
wheat_purchased_hypothesis = 30

# the hypothesis refers to the amount of wheat purchased mentioned in the premise
if wheat_purchased_hypothesis <= wheat_purchased_premise:
    # check if the hypothesis value contradicts the amount of wheat purchased in the premise
    label = "contradiction"
else:
    # the premise gives an exact amount of wheat purchased
    # any amount of wheat greater than 'wheat_purchased_premise' contradicts the premise
    label = "contradiction"

print(label)
