birds_premise = 14.0
more_birds_premise = 21.0
total_birds_hypothesis = 35.0

# the hypothesis refers to the total number of birds, which are also mentioned in the premise
# compute the total number of birds in the premise
total_birds_premise = birds_premise + more_birds_premise
if total_birds_hypothesis!= total_birds_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
