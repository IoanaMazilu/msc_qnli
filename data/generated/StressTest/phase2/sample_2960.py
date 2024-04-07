# Premise: If the boys at Jones Elementary make up 70% of the total school population of x students, what is x?
# Hypothesis: If the boys at Jones Elementary make up 60% of the total school population of x students, what is x?
# Golden Label: contradiction

boys_percentage_premise = 70
boys_percentage_hypothesis = 60

# the hypothesis refers to the percentage of boys in the total school population, same as the premise
if boys_percentage_hypothesis != boys_percentage_premise:
    # if the percentage in the hypothesis contradicts the percentage in the premise, then it's a contradiction
    label = "contradiction"
else:
    # the hypothesis values do not contradict the premise ones, so we can infer entailment
    label = "entailment"

print(label)

