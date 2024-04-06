# Premise: Italy's Civil Protection agency reported at least 1,500 injured and 50,000 without shelter.
# Hypothesis: About 50,000 people without shelter, Italy's Civil Protection agency says.
# Golden Label: entailment

injured_premise = 1500
without_shelter_premise = 50000
without_shelter_hypothesis = 50000

# the hypothesis only mentions the number of people without shelter, which is also referenced in the premise
if without_shelter_hypothesis != without_shelter_premise:
    # check if the number of people without shelter in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
