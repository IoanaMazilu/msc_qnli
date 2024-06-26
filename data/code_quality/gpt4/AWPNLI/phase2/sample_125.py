birds_initial_premise = 2.0
birds_joined_premise = 4.0
birds_hypothesis = 10.0

# the hypothesis refers to the total number of birds, which are also calculated in the premise
# compute the total number of birds in the premise
total_birds_premise = birds_initial_premise + birds_joined_premise
if birds_hypothesis != total_birds_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
