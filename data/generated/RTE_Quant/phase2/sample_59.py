# Premise: Some 420 people have been hanged in Singapore since 1991, mostly for drug trafficking, an Amnesty International 2004 report said. That gives the country of 4.4 million people the highest execution rate in the world relative to population.
# Hypothesis: 4.4 million people live in Singapore.
# Golden Label: entailment

people_executed_premise = 420
population_premise = 4.4e6
population_hypothesis = 4.4e6

# the hypothesis talks about the population of Singapore, which is also mentioned in the premise
if population_hypothesis != population_premise:
    # check if the population in the hypothesis contradicts the population in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

