joan_oranges = 37.0
sara_oranges = 10.0
alyssa_pears = 30.0
total_oranges = joan_oranges + sara_oranges + alyssa_pears

# the hypothesis mentions the total number of oranges picked, which is also mentioned in the premise
# compute the total number of oranges from the premise
total_oranges_premise = joan_oranges + sara_oranges + alyssa_pears
if total_oranges!= total_oranges_premise:
    # check if the total number of oranges in the hypothesis contradicts the total number of oranges in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are the same, we can infer entailment
    label = "entailment"

print(label)
