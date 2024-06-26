people_executed_premise = 420
population_premise = 4.4e6
people_executed_hypothesis = 4.4e6

# the hypothesis talks about the number of people executed in Singapore which is also mentioned in the premise
if people_executed_hypothesis!= people_executed_premise:
    # check if the number of people executed in the hypothesis contradicts the number of people executed from the premise
    label = "contradiction"
elif population_hypothesis!= population_premise:
    # check if the population in the hypothesis contradicts the population in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
