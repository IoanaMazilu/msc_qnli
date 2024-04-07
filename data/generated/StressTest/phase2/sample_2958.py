# Premise: If the boys at Jones Elementary make up 70% of the total school population of x students, what is x?
# Hypothesis: If the boys at Jones Elementary make up more than 60% of the total school population of x students, what is x?
# Golden Label: entailment

boys_percentage_premise = 70
boys_percentage_hypothesis = 60

# the hypothesis talks about the percentage of boys at Jones Elementary, referenced also in the premise
if boys_percentage_hypothesis >= boys_percentage_premise:
    # check if the hypothesis value contradicts the estimate of 'boys_percentage_premise'
    label = "contradiction"
else:
    # the premise gives a specific percentage for the boys population
    # any percentage less than 'boys_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

