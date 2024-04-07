# Premise: If the boys at Jones Elementary make up 20% of the total school population of x students, what is x?
# Hypothesis: If the boys at Jones Elementary make up less than 60% of the total school population of x students, what is x?
# Golden Label: entailment

boys_percentage_premise = 20
boys_percentage_hypothesis = 60

# the hypothesis talks about the percentage of boys at Jones Elementary, referenced also in the premise
if boys_percentage_hypothesis < boys_percentage_premise:
    # check if the hypothesis value contradicts the 'boys_percentage_premise'
    label = "contradiction"
else:
    # the premise gives an exact percentage for the boys population, 
    # any percentage of boys equal to or greater than 'boys_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

