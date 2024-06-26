# define variables for the number of seasons played by Jones
seasons_premise = 12
seasons_hypothesis = 12

# check if the number of seasons in the hypothesis contradicts the number of seasons in the premise
if seasons_hypothesis!= seasons_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
