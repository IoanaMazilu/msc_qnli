# Premise: If the boys at Jones Elementary make up 30% of the total school population of x students, what is x?
# Hypothesis: If the boys at Jones Elementary make up less than 30% of the total school population of x students, what is x?
# Golden Label: contradiction

boys_percentage_premise = 30
boys_percentage_hypothesis = 30

# the hypothesis talks about the percentage of boys at Jones Elementary, referenced also in the premise
if boys_percentage_hypothesis < boys_percentage_premise:
    # check if the hypothesis value contradicts the percentage value mentioned in the premise
    label = "contradiction"
elif boys_percentage_hypothesis > boys_percentage_premise:
    # check if the hypothesis value contradicts the percentage value mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates are the same as the premise ones, we can infer entailment
    label = "entailment"

print(label)

