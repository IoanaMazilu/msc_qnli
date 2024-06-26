# define variables for the numerical entities in the premise and hypothesis
score_premise = 2
score_hypothesis = 2

# check if the score in the hypothesis contradicts the score in the premise
if score_hypothesis!= score_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
