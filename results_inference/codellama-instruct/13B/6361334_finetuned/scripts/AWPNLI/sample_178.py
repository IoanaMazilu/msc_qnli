marbles_premise = 16.0
lost_marbles_premise = 7.0
marbles_hypothesis = 9.0

# the hypothesis refers to the number of marbles, which are also mentioned in the premise
# compute the total number of marbles in the premise
total_marbles_premise = marbles_premise - lost_marbles_premise
if marbles_hypothesis!= total_marbles_premise:
    # check if the number of marbles in the hypothesis contradicts the number of marbles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
