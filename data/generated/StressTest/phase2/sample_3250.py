# Premise: If the boys at Jones Elementary make up less than 60% of the total school population of x students, what is x?
# Hypothesis: If the boys at Jones Elementary make up 20% of the total school population of x students, what is x?
# Golden Label: neutral

boys_percentage_premise = 60
boys_percentage_hypothesis = 20

# the hypothesis talks about the percentage of boys at Jones Elementary, also mentioned in the premise
if boys_percentage_hypothesis >= boys_percentage_premise:
    # check if the hypothesis value contradicts the premise that the boys make up less than 'boys_percentage_premise'
    label = "contradiction"
else:
    # the premise gives an upper limit for the boys' percentage
    # any percentage less than 'boys_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

