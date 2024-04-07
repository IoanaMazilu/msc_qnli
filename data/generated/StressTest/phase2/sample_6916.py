# Premise: Carolyn bought less than 87 gumballs, Lew bought 12 gumballs, and Carey bought X gumballs.
# Hypothesis: Carolyn bought 17 gumballs, Lew bought 12 gumballs, and Carey bought X gumballs.
# Golden Label: neutral

gumballs_carolyn_premise = 87
gumballs_carolyn_hypothesis = 17
gumballs_lew_premise = 12
gumballs_lew_hypothesis = 12

# the hypothesis talks about the number of gumballs Carolyn, Lew and Carey bought, referenced also in the premise
if gumballs_carolyn_hypothesis >= gumballs_carolyn_premise:
    # check if the hypothesis value contradicts the estimate of less than 'gumballs_carolyn_premise'
    label = "contradiction"
elif gumballs_lew_hypothesis != gumballs_lew_premise:
    # check if the number of gumballs Lew bought in the hypothesis contradicts the number of gumballs Lew bought reported in the premise
    label = "contradiction"
else:
    # the number of gumballs Carolyn and Lew bought in the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise 
    label = "neutral"

print(label)

