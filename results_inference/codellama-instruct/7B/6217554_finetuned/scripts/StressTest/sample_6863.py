# define the variables for the distances and the time
distance_premise = 45
distance_hypothesis = 85
time_premise = 1
time_hypothesis = 1

# check if the hypothesis values contradict the premise ones
if distance_hypothesis!= distance_premise:
    label = "contradiction"
elif time_hypothesis!= time_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
