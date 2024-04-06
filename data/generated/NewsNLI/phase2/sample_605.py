# Premise: Twenty-nine people in the northwest Alabama town of nearly 1,600 residents died, according to Marion County Sheriff Kevin Williams.
# Hypothesis: Thirty-five people killed in Marion County, sheriff says.
# Golden Label: neutral

people_died_premise = 29
people_killed_hypothesis = 35

# the hypothesis mentions the number of people killed in Marion County, which is also mentioned in the premise
if people_killed_hypothesis != people_died_premise:
    # check if the number of people killed in the hypothesis contradicts the number of people died reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

