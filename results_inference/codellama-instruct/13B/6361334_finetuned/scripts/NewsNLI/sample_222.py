# define variables for the numerical entities in the premise and hypothesis
killed_premise = 2
killed_hypothesis = 2
wounded_premise = 2
wounded_hypothesis = 2

# check if the number of killed and wounded in the hypothesis contradicts the number of killed and wounded in the premise
if killed_hypothesis!= killed_premise or wounded_hypothesis!= wounded_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
