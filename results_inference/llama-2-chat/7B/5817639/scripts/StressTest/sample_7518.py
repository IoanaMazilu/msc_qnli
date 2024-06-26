population_premise = 30
population_hypothesis = 10

# the hypothesis talks about the percentage of boys in a school population, referenced also in the premise
if population_hypothesis <= population_premise:
    # check if the hypothesis value contradicts the estimate of 'population_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of boys
    # any percentage of boys greater than 'population_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
