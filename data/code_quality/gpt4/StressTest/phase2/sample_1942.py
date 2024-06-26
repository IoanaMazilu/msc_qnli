chocolate_flavors_premise = 1
chocolate_flavors_hypothesis = 5

# the hypothesis talks about the number of chocolate flavors John has in his shop, referenced also in the premise
if chocolate_flavors_hypothesis <= chocolate_flavors_premise:
    # check if the hypothesis value contradicts the estimate of more than 'chocolate_flavors_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of chocolate flavors
    # any number of flavors greater than 'chocolate_flavors_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
