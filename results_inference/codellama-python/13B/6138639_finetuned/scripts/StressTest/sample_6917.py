carolyn_gumballs_premise = 17
carolyn_gumballs_hypothesis = 57
lew_gumballs_premise = 12
lew_gumballs_hypothesis = 12
carey_gumballs_premise = 0
carey_gumballs_hypothesis = 0

# the hypothesis talks about the number of gumballs bought by Carolyn, Lew, and Carey, referenced also in the premise
if carolyn_gumballs_hypothesis!= carolyn_gumballs_premise:
    # check if the number of gumballs bought by Carolyn in the hypothesis contradicts the number of gumballs bought by Carolyn in the premise
    label = "contradiction"
elif lew_gumballs_hypothesis!= lew_gumballs_premise:
    # check if the number of gumballs bought by Lew in the hypothesis contradicts the number of gumballs bought by Lew in the premise
    label = "contradiction"
elif carey_gumballs_hypothesis!= carey_gumballs_premise:
    # check if the number of gumballs bought by Carey in the hypothesis contradicts the number of gumballs bought by Carey in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
