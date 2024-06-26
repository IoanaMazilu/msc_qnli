# define variables for the numerical entities in the premise and hypothesis
premise_killed = 2
premise_wounded = 2
hypothesis_killed = 2
hypothesis_injured = 2

# check if the number of killed and wounded in the hypothesis contradicts the number of killed and wounded in the premise
if hypothesis_killed!= premise_killed or hypothesis_injured!= premise_wounded:
    label = "contradiction"
else:
    label = "entailment"

print(label)
