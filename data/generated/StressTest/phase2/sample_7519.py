# Premise: If the boys at Jones Elementary make up more than 10% of the total school population of x students, what is x?
# Hypothesis: If the boys at Jones Elementary make up 30% of the total school population of x students, what is x?
# Golden Label: neutral

boys_percentage_premise = 10
boys_percentage_hypothesis = 30

# the hypothesis refers to the percentage of boys at Jones Elementary in the total school population, also mentioned in the premise
if boys_percentage_hypothesis <= boys_percentage_premise:
    # check if the hypothesis percentage contradicts the estimate of more than 'boys_percentage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of boys
    # any percentage greater than 'boys_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

