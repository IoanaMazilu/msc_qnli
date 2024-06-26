gumballs_carolyn_premise = 46
gumballs_carolyn_hypothesis = 16
gumballs_lew_premise = 14
gumballs_lew_hypothesis = 14
gumballs_carey_premise = X
gumballs_carey_hypothesis = X

# the hypothesis talks about the number of gumballs bought by each person, referenced also in the premise
if gumballs_carolyn_hypothesis <= gumballs_carolyn_premise:
    # check if the hypothesis value contradicts the estimate of less than 'gumballs_carolyn_premise'
    label = "contradiction"
elif gumballs_lew_hypothesis!= gumballs_lew_premise:
    # check if the number of gumballs bought by Lew in the hypothesis contradicts the number of gumballs bought by Lew reported in the premise
    label = "contradiction"
elif gumballs_carey_hypothesis!= gumballs_carey_premise:
    # check if the number of gumballs bought by Carey in the hypothesis contradicts the number of gumballs bought by Carey reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
