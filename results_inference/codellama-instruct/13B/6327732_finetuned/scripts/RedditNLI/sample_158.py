# define variables for the premise and hypothesis
premise_factors = 5
hypothesis_factors = 5

# check if the number of factors in the hypothesis contradicts the number of factors in the premise
if hypothesis_factors!= premise_factors:
    label = "contradiction"
else:
    label = "neutral"

print(label)