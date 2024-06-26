population_premise = 4.4e6
population_hypothesis = 4.4e6

# the hypothesis talks about the total number of people executed in Singapore, which is also mentioned in the premise
# the premise gives the number of people executed in Singapore relative to the population, so we need to convert the number of executions to a percentage
execution_rate_premise = 420 / population_premise

# the hypothesis provides the total number of people executed, so we can calculate the execution rate
execution_rate_hypothesis = population_hypothesis / 420

# compare the execution rates calculated from the premise and the hypothesis
if execution_rate_hypothesis!= execution_rate_premise:
    # check if the execution rate in the hypothesis contradicts the execution rate calculated from the premise
    label = "contradiction"
else:
    # if the execution rates do not contradict, we can infer entailment
    label = "entailment"

print(label)
