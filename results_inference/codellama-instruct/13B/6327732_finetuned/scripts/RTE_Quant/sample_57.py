population_premise = 4.4e6
execution_rate_premise = 420 / population_premise
population_hypothesis = 4.4e6
execution_rate_hypothesis = 420 / population_hypothesis

# the hypothesis talks about the number of executions in Singapore, which is not mentioned in the premise
# the hypothesis cannot be entailed from the premise, since the number of executions is unknown.
label = "neutral"

print(label)
