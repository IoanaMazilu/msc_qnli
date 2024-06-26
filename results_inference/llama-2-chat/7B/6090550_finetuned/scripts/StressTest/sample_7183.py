# North America passengers
n_north_america_premise = 4/12
n_north_america_hypothesis = 1/12
if n_north_america_hypothesis!= n_north_america_premise:
    # check if the number of North American passengers in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of North American passengers in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
