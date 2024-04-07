# Premise: If the boys at Jones Elementary make up more than 60% of the total school population of x students, what is x?
# Hypothesis: If the boys at Jones Elementary make up 70% of the total school population of x students, what is x?
# Golden Label: neutral

boy_percentage_premise = 60
boy_percentage_hypothesis = 70

# the hypothesis talks about the percentage of boys at Jones Elementary, which is also referenced in the premise
if boy_percentage_hypothesis <= boy_percentage_premise:
    # check if the hypothesis value contradicts the estimate of more than 'boy_percentage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of boys
    # any percentage greater than 'boy_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

