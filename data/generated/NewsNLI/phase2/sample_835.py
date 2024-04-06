# Premise: Stenson's two-shot lead evaporated when he fired a one-over 73 and he finished tied for second with Denmark's JB Hansen.
# Hypothesis: Scandinavians JB Hansen and Henrik Stenson finish two shots behind Mickelson and Grace.
# Golden Label: neutral

stenson_shots_premise = 1
stenson_shots_hypothesis = 2
hansen_shots_premise = 2
hansen_shots_hypothesis = 2

# the hypothesis mentions the number of shots behind of both Stenson and Hansen, which are also mentioned in the premise
# however, the hypothesis also mentions two players, Mickelson and Grace, which cannot be entailed from the premise
if stenson_shots_hypothesis != stenson_shots_premise:
    # check if the number of shots behind of Stenson in the hypothesis contradicts the number of shots behind of Stenson in the premise
    label = "contradiction"
elif hansen_shots_hypothesis != hansen_shots_premise:
    # check if the number of shots behind of Hansen in the hypothesis contradicts the number of shots behind of Hansen in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we infer neutrality due to additional players mentioned in the hypothesis
    label = "neutral"

print(label)

