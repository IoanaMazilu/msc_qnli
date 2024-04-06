# Premise: Police:Bombings kill 5 in Iraq, wound dozens more.
# Hypothesis: Bombings kill at least 18, wound dozens.
# Golden Label: neutral

killed_premise = 5
killed_hypothesis = 18
wounded_premise = 30 # assuming dozens means at least 2 dozens
wounded_hypothesis = 30

# the hypothesis mentions the number of people killed and wounded, which are also mentioned in the premise
if killed_hypothesis < killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif wounded_hypothesis != wounded_premise:
    # check if the number of people wounded from the hypothesis contradicts the number of people wounded in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "neutral"

print(label)

