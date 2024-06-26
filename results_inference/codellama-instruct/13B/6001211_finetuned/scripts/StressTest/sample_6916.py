gumballs_carolyn_premise = 87
gumballs_carolyn_hypothesis = 17
gumballs_lew_premise = 12
gumballs_lew_hypothesis = 12

# the hypothesis refers to the number of gumballs bought by Carolyn, Lew, and Carey, mentioned in the premise
if gumballs_carolyn_hypothesis >= gumballs_carolyn_premise:
    # check if the number of gumballs bought by Carolyn in the hypothesis contradicts the estimate of less than 'gumballs_carolyn_premise'
    label = "contradiction"
elif gumballs_lew_hypothesis!= gumballs_lew_premise:
    # check if the number of gumballs bought by Lew in the hypothesis contradicts the number of gumballs bought by Lew in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gumballs bought by Carolyn
    # any number of gumballs less than 'gumballs_carolyn_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
