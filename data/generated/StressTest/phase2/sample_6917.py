# Premise: Carolyn bought 17 gumballs, Lew bought 12 gumballs, and Carey bought X gumballs.
# Hypothesis: Carolyn bought 57 gumballs, Lew bought 12 gumballs, and Carey bought X gumballs.
# Golden Label: contradiction

carolyn_gumballs_premise = 17
lew_gumballs_premise = 12
carey_gumballs_premise = 'X'

carolyn_gumballs_hypothesis = 57
lew_gumballs_hypothesis = 12
carey_gumballs_hypothesis = 'X'

# the hypothesis mentions the gumballs bought by Carolyn, Lew, and Carey, referenced also in the premise
if carolyn_gumballs_hypothesis != carolyn_gumballs_premise:
    # check if the number of gumballs Carolyn bought in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif lew_gumballs_hypothesis != lew_gumballs_premise:
    # check if the number of gumballs Lew bought in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif carey_gumballs_hypothesis != carey_gumballs_premise:
    # check if the number of gumballs Carey bought in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

