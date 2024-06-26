population_premise = 30
population_hypothesis = 10

# the hypothesis refers to the percentage of boys in the total school population
if population_hypothesis <= population_premise:
    # check if the hypothesis value contradicts the premise percentage
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of boys in the total school population
    # any percentage greater than 'population_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
