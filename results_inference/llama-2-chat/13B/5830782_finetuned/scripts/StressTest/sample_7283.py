gumballs_carolyn_premise = 16
gumballs_lew_premise = 14
gumballs_carey_premise = 'X'

gumballs_carolyn_hypothesis = 66
gumballs_lew_hypothesis = 14
gumballs_carey_hypothesis = 'X'

# the hypothesis refers to the number of gumballs bought by Carolyn, Lew and Carey mentioned in the premise
if gumballs_carolyn_premise!= gumballs_carolyn_hypothesis:
    # check if the number of gumballs bought by Carolyn in the hypothesis contradicts the number of gumballs bought by Carolyn in the premise
    label = "contradiction"
elif gumballs_lew_premise!= gumballs_lew_hypothesis:
    # check if the number of gumballs bought by Lew in the hypothesis contradicts the number of gumballs bought by Lew in the premise
    label = "contradiction"
elif gumballs_carey_hypothesis!= gumballs_carey_premise:
    # check if the number of gumballs bought by Carey in the hypothesis contradicts the number of gumballs bought by Carey in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
