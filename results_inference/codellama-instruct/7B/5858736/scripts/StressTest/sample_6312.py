# Define variables for the premise and hypothesis
males_premise = 4
females_premise = 3
mary_premise = "Mary wants to sit with her back on the wall"

# Define variables for the hypothesis
males_hypothesis = 2
females_hypothesis = 3
mary_hypothesis = "Mary wants to sit with her back on the wall"

# Check if the hypothesis values contradict the premise values
if males_hypothesis > males_premise or females_hypothesis > females_premise:
    label = "contradiction"
elif mary_hypothesis!= mary_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
