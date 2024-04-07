# Premise: If the boys at Jones Elementary make up 20% of the total school population of x students, what is x?
# Hypothesis: If the boys at Jones Elementary make up more than 20% of the total school population of x students, what is x?
# Golden Label: contradiction

boys_percentage_premise = 20
boys_percentage_hypothesis = 20

# the hypothesis refers to the percentage of boys in the elementary school, also mentioned in the premise
if boys_percentage_hypothesis <= boys_percentage_premise:
    # check if the estimate of 'boys_percentage_hypothesis' contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of boys
    # any percentage greater than 'boys_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

