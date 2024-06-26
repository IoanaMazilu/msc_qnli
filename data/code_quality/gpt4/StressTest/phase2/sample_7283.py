carolyn_gumballs_premise = 16
lew_gumballs_premise = 14
carey_gumballs_premise = 'X'

carolyn_gumballs_hypothesis = 66
lew_gumballs_hypothesis = 14
carey_gumballs_hypothesis = 'X'

# the hypothesis talks about the number of gumballs bought by each person, referenced also in the premise
if carolyn_gumballs_premise != carolyn_gumballs_hypothesis:
    # check if the number of gumballs bought by Carolyn in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif lew_gumballs_premise != lew_gumballs_hypothesis:
    # check if the number of gumballs bought by Lew in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif carey_gumballs_premise != carey_gumballs_hypothesis:
    # check if the number of gumballs bought by Carey in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
