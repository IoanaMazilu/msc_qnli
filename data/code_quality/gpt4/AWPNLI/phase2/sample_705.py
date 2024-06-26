mary_marbles_premise = 9.0
given_marbles_premise = 3.0
mary_marbles_hypothesis = 7.0

# the hypothesis refers to the number of marbles Mary has left, which is also mentioned in the premise
# compute how many marbles Mary has left according to the premise
mary_marbles_left_premise = mary_marbles_premise - given_marbles_premise
if mary_marbles_hypothesis != mary_marbles_left_premise:
    # check if the number of marbles left in the hypothesis contradicts the number of marbles left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
