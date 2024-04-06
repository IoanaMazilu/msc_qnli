# Premise: The world's population is set to reach a staggering 10bn by the middle of the next century up from 5.7bn now.
# Hypothesis: The current world population is 5.7 billion.
# Golden Label: entailment

population_future_premise = 10e9
population_current_premise = 5.7e9
population_current_hypothesis = 5.7e9

# the hypothesis talks about the current population of the world, which is also mentioned in the premise
if population_current_hypothesis != population_current_premise:
    # check if the current population in the hypothesis contradicts the current population from the premise
    label = "contradiction"
else:
    # if the current population in the hypothesis does not contradict the current population from the premise, we can infer entailment
    label = "entailment"

print(label)

