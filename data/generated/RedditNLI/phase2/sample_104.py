# Premise: 85 richest people own as much as bottom half of population, report says.
# Hypothesis: 85 richest people as wealthy as half of the worlds population.
# Golden Label: entailment

num_richest_people_premise = 85
num_richest_people_hypothesis = 85
population_percentage_premise = 50
population_percentage_hypothesis = 50

# the hypothesis and premise mention the number of the richest people and the percentage of the population they are as wealthy as 
if num_richest_people_premise != num_richest_people_hypothesis:
    # check if the number of the richest people in the hypothesis contradicts the number of the richest people in the premise
    label = "contradiction"
elif population_percentage_premise != population_percentage_hypothesis:
    # check if the population percentage in the hypothesis contradicts the population percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

