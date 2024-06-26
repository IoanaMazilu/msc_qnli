# define variables for the numerical entities in the premise
num_killed_premise = 4
num_wounded_premise = 80

# define variables for the numerical entities in the hypothesis
num_killed_hypothesis = 4
num_wounded_hypothesis = 80

# check if the number of killed and wounded in the hypothesis contradicts the number of killed and wounded in the premise
if num_killed_hypothesis!= num_killed_premise or num_wounded_hypothesis!= num_wounded_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
