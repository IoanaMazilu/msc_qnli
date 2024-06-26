# Define variables for the numerical entities in the premise and hypothesis
wounded_workers_premise = 4
serious_condition_premise = 4

wounded_workers_hypothesis = 4
serious_condition_hypothesis = 4

# Check if the number of wounded workers in the hypothesis contradicts the number of wounded workers in the premise
if wounded_workers_hypothesis!= wounded_workers_premise:
    # If the number of wounded workers in the hypothesis contradicts the number of wounded workers in the premise, we can infer contradiction
    label = "contradiction"
else:
    # If the number of wounded workers in the hypothesis does not contradict the number of wounded workers in the premise, we can infer entailment
    label = "entailment"

print(label)
