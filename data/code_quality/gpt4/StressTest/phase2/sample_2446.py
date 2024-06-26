product_ages_premise = 72
product_ages_hypothesis = 32

# the hypothesis refers to the product of Diana's and a third of Rashid's age, which is also mentioned in the premise
if product_ages_hypothesis >= product_ages_premise:
    # check if the hypothesis value contradicts the premise of the product being less than 'product_ages_premise'
    label = "contradiction"
elif product_ages_hypothesis < product_ages_premise:
    # the premise gives only an upper limit for the product of the ages
    # any product less than 'product_ages_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
