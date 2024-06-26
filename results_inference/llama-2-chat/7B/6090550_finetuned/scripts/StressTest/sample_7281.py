gumballs_carolyn_premise = 16
gumballs_carolyn_hypothesis = 46
gumballs_lew_premise = 14
gumballs_lew_hypothesis = 14
gumballs_carey_premise = X
gumballs_carey_hypothesis = X

# the hypothesis talks about the number of gumballs bought by Carolyn, Lew and Carey
if gumballs_carolyn_premise >= gumballs_carolyn_hypothesis:
    label = "entailment"
elif gumballs_lew_premise!= gumballs_lew_hypothesis:
    label = "contradiction"
elif gumballs_carey_premise!= gumballs_carey_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
