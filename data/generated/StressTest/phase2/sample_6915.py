# Premise: Carolyn bought 17 gumballs, Lew bought 12 gumballs, and Carey bought X gumballs.
# Hypothesis: Carolyn bought less than 87 gumballs, Lew bought 12 gumballs, and Carey bought X gumballs.
# Golden Label: entailment

gumballs_carolyn_premise = 17
gumballs_carolyn_hypothesis = 87
gumballs_lew_premise = 12
gumballs_lew_hypothesis = 12

# the hypothesis refers to the number of gumballs bought by Carolyn and Lew mentioned in the premise
if gumballs_carolyn_premise >= gumballs_carolyn_hypothesis:
    # check if the estimate of 'gumballs_carolyn_hypothesis' contradicts the number of gumballs bought by Carolyn in the premise
    label = "contradiction"
elif gumballs_lew_hypothesis != gumballs_lew_premise:
    # check if the number of gumballs bought by Lew in the hypothesis contradicts the number of gumballs bought by Lew reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

