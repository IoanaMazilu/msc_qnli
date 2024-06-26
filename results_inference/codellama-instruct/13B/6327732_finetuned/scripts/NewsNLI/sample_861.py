# define variables for the numerical entities in the premise and hypothesis
premise_age = 85
hypothesis_age = 85

# check if the age in the hypothesis contradicts the age in the premise
if hypothesis_age!= premise_age:
    label = "contradiction"
else:
    label = "entailment"

print(label)
