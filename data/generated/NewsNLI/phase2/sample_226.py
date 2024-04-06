# Premise: Over 1.8 million people of Japanese descent live in Brazil, 600,000 of them concentrated in Liberdade.
# Hypothesis: Brazil is home to 1.8 million people of Japanese descent.
# Golden Label: entailment

japanese_descent_population_premise = 1800000
japanese_descent_population_hypothesis = 1800000

# the hypothesis mentions the total population of people of Japanese descent in Brazil, which is also mentioned in the premise
if japanese_descent_population_hypothesis != japanese_descent_population_premise:
    # check if the population of people of Japanese descent in the hypothesis contradicts the population of people of Japanese descent in the premise
    label = "contradiction"
else:
    # if the hypothesis population does not contradict the premise population, we can infer entailment
    label = "entailment"

print(label)

