# define variables for the numerical entities in the premise and hypothesis
premise_score = 83
hypothesis_score = 30

# check if the hypothesis score contradicts the premise score
if hypothesis_score <= premise_score:
    label = "contradiction"
else:
    label = "neutral"

print(label)
