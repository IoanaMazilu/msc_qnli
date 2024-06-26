premise_percentage = 30
hypothesis_percentage = 10

# the hypothesis refers to the percentage of boys in the total school population
if hypothesis_percentage <= premise_percentage:
    # check if the hypothesis value contradicts the premise percentage
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of boys in the total school population
    # any percentage greater than 'premise_percentage' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
