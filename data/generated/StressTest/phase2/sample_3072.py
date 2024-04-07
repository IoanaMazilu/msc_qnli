# Premise: If the boys at Jones Elementary make up 60% of the total school population of x students, what is x?
# Hypothesis: If the boys at Jones Elementary make up more than 40% of the total school population of x students, what is x?
# Golden Label: entailment

boys_percentage_premise = 60
boys_percentage_hypothesis = 40

# the hypothesis refers to the percentage of boys mentioned in the premise
if boys_percentage_hypothesis >= boys_percentage_premise:
    # check if the 'boys_percentage_hypothesis' contradicts the percentage of boys in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

