# define variables for the numerical entities in the premise and hypothesis
points_premise = 1
points_hypothesis = 0

# check if the points scored by Norwich in the hypothesis contradicts the points scored by Manchester City in the premise
if points_hypothesis!= points_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
