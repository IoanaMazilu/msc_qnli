coffee_ounces_premise = 45
coffee_ounces_hypothesis = 85

# the hypothesis refers to the total ounces of coffee owned by Carina, which is also mentioned in the premise
if coffee_ounces_hypothesis <= coffee_ounces_premise:
    # check if the hypothesis value contradicts the estimate of more than 'coffee_ounces_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total ounces of coffee
    # any number of ounces greater than 'coffee_ounces_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
