birds_premise = 6.0
nests_premise = 3.0
birds_hypothesis = 9.0

# the hypothesis refers to the number of bird-related objects, which is also mentioned in the premise
# compute the total number of birds and nests in the premise
total_birds_premise = birds_premise + nests_premise
if birds_hypothesis!= total_birds_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
