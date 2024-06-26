# define variables for the numerical entities in the premise and hypothesis
marching_100_premise = 100
marching_100_hypothesis = 100

# check if the number of members in the Marching 100 band from the hypothesis contradicts the number of members in the premise
if marching_100_hypothesis!= marching_100_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
