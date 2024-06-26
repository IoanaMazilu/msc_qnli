# The hypothesis refers to the time difference between the trip to the beach and the trip home
time_difference_hypothesis = 1/2

# The premise gives the time difference between the trip to the beach and the trip home
time_difference_premise = 3/2

# If the time difference in the hypothesis is contradicting the time difference in the premise, we can infer entailment
if time_difference_hypothesis!= time_difference_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
