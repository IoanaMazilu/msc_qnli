birds_initial_premise = 2.0
birds_joining_premise = 4.0
total_birds_hypothesis = 6.0

# the hypothesis refers to the total number of birds, which are also mentioned in the premise
# compute the total number of birds in the premise
total_birds_premise = birds_initial_premise + birds_joining_premise
if total_birds_hypothesis != total_birds_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
