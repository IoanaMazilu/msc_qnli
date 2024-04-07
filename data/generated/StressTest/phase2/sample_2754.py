# Premise: Carolyn bought 15 gumballs, Lew bought 12 gumballs, and Carey bought X gumballs.
# Hypothesis: Carolyn bought less than 75 gumballs, Lew bought 12 gumballs, and Carey bought X gumballs.
# Golden Label: entailment

gumballs_carolyn_premise = 15
gumballs_carolyn_hypothesis = 75
gumballs_lew_premise = 12
gumballs_lew_hypothesis = 12

# the hypothesis talks about the number of gumballs bought by Carolyn, Lew, and Carey, referenced also in the premise
if gumballs_carolyn_premise >= gumballs_carolyn_hypothesis:
    # check if the number of gumballs bought by Carolyn in the premise contradicts the estimate of less than 'gumballs_carolyn_hypothesis'
    label = "contradiction"
elif gumballs_lew_premise != gumballs_lew_hypothesis:
    # check if the number of gumballs bought by Lew in the premise contradicts the number of gumballs bought by Lew in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

