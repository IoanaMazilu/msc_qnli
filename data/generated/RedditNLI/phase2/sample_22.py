# Premise: World's 85 richest people have as much as poorest 3.5 billion: Oxfam warns Davos of pernicious impact of the widening wealth gap.
# Hypothesis: Richest 85 people across the globe share a combined wealth of 1tn, as much as the poorest 3.5 billion of the world's population.
# Golden Label: neutral

richest_people_premise = 85
richest_people_hypothesis = 85
poorest_people_premise = 3.5 * 10**9
poorest_people_hypothesis = 3.5 * 10**9

# the hypothesis and premise mention the number of richest and poorest people
if richest_people_premise != richest_people_hypothesis:
    # check if the number of richest people in the hypothesis contradicts the number of richest people in the premise
    label = "contradiction"
elif poorest_people_premise != poorest_people_hypothesis:
    # check if the number of poorest people in the hypothesis contradicts the number of poorest people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

