gumballs_carolyn_premise = 17
gumballs_lew_premise = 12
gumballs_carey_premise = X
gumballs_carolyn_hypothesis = 57
gumballs_lew_hypothesis = 12
gumballs_carey_hypothesis = X

# the hypothesis refers to the number of gumballs bought by each person, referenced also in the premise
if gumballs_carolyn_hypothesis <= gumballs_carolyn_premise:
    # check if the estimate of 'gumballs_carolyn_hypothesis' contradicts the number of gumballs bought by Carolyn in the premise
    label = "contradiction"
elif gumballs_lew_hypothesis!= gumballs_lew_premise:
    # check if the number of gumballs bought by Lew in the hypothesis contradicts the number of gumballs bought by Lew in the premise
    label = "contradiction"
elif gumballs_carey_hypothesis!= gumballs_carey_premise:
    # check if the number of gumballs bought by Carey in the hypothesis contradicts the number of gumballs bought by Carey in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)