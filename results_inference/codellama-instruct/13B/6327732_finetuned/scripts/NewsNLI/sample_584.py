# define variables for the numerical entities in the premise and hypothesis
premise_matches = 7
hypothesis_matches = 5

# check if the number of matches in the hypothesis contradicts the number of matches in the premise
if hypothesis_matches!= premise_matches:
    label = "contradiction"
else:
    label = "neutral"

print(label)
