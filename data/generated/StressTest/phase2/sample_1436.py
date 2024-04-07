# Premise: Carolyn bought 16 gumballs, Lew bought 12 gumballs, and Bob bought X gumballs.
# Hypothesis: Carolyn bought 46 gumballs, Lew bought 12 gumballs, and Bob bought X gumballs.
# Golden Label: contradiction

gumballs_carolyn_premise = 16
gumballs_lew_premise = 12
gumballs_bob_premise = "X"

gumballs_carolyn_hypothesis = 46
gumballs_lew_hypothesis = 12
gumballs_bob_hypothesis = "X"

# the hypothesis refers to the number of gumballs bought by Carolyn, Lew and Bob in the premise
if gumballs_carolyn_premise != gumballs_carolyn_hypothesis:
    # check if the number of gumballs bought by Carolyn in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif gumballs_lew_premise != gumballs_lew_hypothesis:
    # check if the number of gumballs bought by Lew in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif gumballs_bob_premise != gumballs_bob_hypothesis:
    # check if the number of gumballs bought by Bob in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

