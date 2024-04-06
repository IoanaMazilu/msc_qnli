# Premise: Meanwhile, two U.S. service members were killed and two were wounded in an explosion targeting their vehicle in Wardak province, officials said.
# Hypothesis: Two American service members killed, two others injured in Wardak province blast.
# Golden Label: entailment

killed_members_premise = 2
killed_members_hypothesis = 2
wounded_members_premise = 2
wounded_members_hypothesis = 2

# the hypothesis mentions the number of killed and injured service members, which are also mentioned in the premise
if killed_members_hypothesis != killed_members_premise:
    # check if the number of killed members in the hypothesis contradicts the number of killed members reported in the premise
    label = "contradiction"
elif wounded_members_hypothesis != wounded_members_premise:
    # check if the number of injured members from the hypothesis contradicts the number of injured members in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

