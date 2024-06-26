active_psychiatrists_premise = 50
active_psychiatrists_hypothesis = 50
population_premise = 30000000
population_hypothesis = 30000000

# the hypothesis mentions the number of active psychiatrists in the country, which is also mentioned in the premise
# however, the hypothesis does not mention the population of the country, which is also mentioned in the premise
# therefore, we cannot infer entailment or contradiction from the hypothesis
label = "neutral"

print(label)
