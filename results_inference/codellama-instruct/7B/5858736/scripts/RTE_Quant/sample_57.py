# Define variables for the numerical entities in the premise and hypothesis
total_executions_premise = 420
population_singapore = 4.4e6
execution_rate_premise = total_executions_premise / population_singapore

# Define variables for the numerical entities in the hypothesis
population_singapore_hypothesis = 4.4e6

# Check if the hypothesis contradicts the premise
if execution_rate_premise!= population_singapore_hypothesis:
    # The hypothesis contradicts the premise, so the label is "contradiction"
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
