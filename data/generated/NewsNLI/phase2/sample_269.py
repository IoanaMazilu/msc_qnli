# Premise: At least 21 deaths are confirmed in Pakistan, said Maj. Iftikhar Ahmed Taj of the National Disaster Management Authority.
# Hypothesis: At least 21 people are confirmed dead, says disaster official Maj. Iftikhar Ahmed Taj.
# Golden Label: entailment

deaths_premise = 21
deaths_hypothesis = 21

# the hypothesis mentions the number of confirmed deaths, which is also mentioned in the premise
if deaths_hypothesis != deaths_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
else:
    # if the number of deaths in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

