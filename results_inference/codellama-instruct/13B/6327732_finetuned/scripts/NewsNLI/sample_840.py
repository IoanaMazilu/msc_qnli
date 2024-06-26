# define variables for the entities in the premise and hypothesis
premise_iPads = 2
hypothesis_iPads = 2

# check if the number of iPads in the hypothesis contradicts the number of iPads found in the premise
if hypothesis_iPads!= premise_iPads:
    label = "contradiction"
else:
    label = "entailment"

print(label)
