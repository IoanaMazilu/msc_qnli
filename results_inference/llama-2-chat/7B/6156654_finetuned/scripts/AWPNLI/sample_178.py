marbles_josh_premise = 16.0
lost_marbles_josh_premise = 7.0
new_marbles_josh_hypothesis = 9.0

# the hypothesis refers to the number of marbles Josh has now, which is also mentioned in the premise
# compute the current number of marbles Josh has in the premise
current_marbles_josh_premise = marbles_josh_premise - lost_marbles_josh_premise
if new_marbles_josh_hypothesis!= current_marbles_josh_premise:
    # check if the number of marbles in the hypothesis contradicts the number of marbles in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are equal, we can infer entailment
    label = "entailment"

print(label)
