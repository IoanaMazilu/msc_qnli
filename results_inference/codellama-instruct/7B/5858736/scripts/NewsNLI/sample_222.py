# Define variables for the numerical entities in the premise and hypothesis
premise_killed = 2
premise_wounded = 2
hypothesis_killed = 2
hypothesis_wounded = 2

# Extract all quantities as valid numbers
killed_premise = int(premise_killed)
wounded_premise = int(premise_wounded)
killed_hypothesis = int(hypothesis_killed)
wounded_hypothesis = int(hypothesis_wounded)

# Check if the hypothesis values and estimates do not contradict the premise values
if killed_hypothesis!= killed_premise or wounded_hypothesis!= wounded_premise:
    # If the hypothesis values and estimates contradict the premise values, we can infer contradiction
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
