# define variables for the numerical entities in the premise and hypothesis
elevation_premise = 1000
population_premise = 2000000
elevation_hypothesis = 1000
population_hypothesis = 2000000

# check if the population in the hypothesis contradicts the population in the premise
if population_hypothesis!= population_premise:
    label = "contradiction"
# check if the elevation in the hypothesis contradicts the elevation in the premise
elif elevation_hypothesis!= elevation_premise:
    label = "contradiction"
# if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
else:
    label = "entailment"

print(label)
