# Premise: Paris (CNN) Police found the bodies of five infants in a home near Bordeaux, France, according to news reports.
# Hypothesis: Reports say police find bodies of five newborns in home in southwestern France.
# Golden Label: neutral

bodies_found_premise = 5
bodies_found_hypothesis = 5

# the hypothesis mentions the number of infant bodies found, which is also referenced in the premise
if bodies_found_hypothesis != bodies_found_premise:
    # check if the number of bodies found in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of bodies found does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

