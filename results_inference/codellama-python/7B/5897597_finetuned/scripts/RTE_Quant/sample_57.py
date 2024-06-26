total_people_hanged_premise = 420
population_premise = 4.4e6
total_people_executed_hypothesis = 4.4e6

# the hypothesis talks about the total number of people executed in Singapore, which is also mentioned in the premise
if total_people_executed_hypothesis!= total_people_hanged_premise:
    # check if the total number of people executed in the hypothesis contradicts the total number of people hanged from the premise
    label = "contradiction"
elif population_premise!= total_people_executed_hypothesis:
    # check if the population in the hypothesis contradicts the total number of people executed in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
