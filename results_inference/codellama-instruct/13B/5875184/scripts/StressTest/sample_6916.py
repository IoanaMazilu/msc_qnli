carolyn_gumballs_premise = 87
lew_gumballs_premise = 12
carey_gumballs_premise = X

carolyn_gumballs_hypothesis = 17
lew_gumballs_hypothesis = 12
carey_gumballs_hypothesis = X

# the hypothesis refers to the number of gumballs bought by Carolyn and Lew, which are also mentioned in the premise
if carolyn_gumballs_hypothesis <= carolyn_gumballs_premise and lew_gumballs_hypothesis == lew_gumballs_premise:
    # check if the hypothesis values contradict the premise estimates
    label = "contradiction"
elif carey_gumballs_hypothesis!= carey_gumballs_premise:
    # check if the number of gumballs bought by Carey in the hypothesis contradicts the number of gumballs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
