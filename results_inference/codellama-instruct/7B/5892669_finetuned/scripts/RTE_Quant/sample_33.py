population_future_premise = 10e9
population_now_premise = 5.7e9
population_now_hypothesis = 5.7e9

# the hypothesis talks about the current world population, which is also mentioned in the premise
if population_now_hypothesis!= population_now_premise:
    # check if the current population in the hypothesis contradicts the current population in the premise
    label = "contradiction"
else:
    # if the current population in the hypothesis does not contradict the current population in the premise, we can infer entailment
    label = "entailment"

print(label)
