gumballs_bought_premise = 46
gumballs_bought_hypothesis = 16
gumballs_bought_lew_premise = 14
gumballs_bought_lew_hypothesis = 14
gumballs_bought_carey_premise = 0
gumballs_bought_carey_hypothesis = 0

# the hypothesis talks about the number of gumballs bought by Carolyn, Lew, and Carey, referenced also in the premise
if gumballs_bought_hypothesis <= gumballs_bought_premise:
    # check if the hypothesis value contradicts the estimate of less than 'gumballs_bought_premise'
    label = "contradiction"
elif gumballs_bought_lew_hypothesis!= gumballs_bought_lew_premise:
    # check if the number of gumballs bought by Lew in the hypothesis contradicts the number of gumballs bought by Lew reported in the premise
    label = "contradiction"
elif gumballs_bought_carey_hypothesis!= gumballs_bought_carey_premise:
    # check if the number of gumballs bought by Carey in the hypothesis contradicts the number of gumballs bought by Carey reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
