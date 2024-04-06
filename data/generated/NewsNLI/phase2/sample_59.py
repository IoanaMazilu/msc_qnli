# Premise: The Syria Human Rights Information Link told CNN that at least 11 people died in the western industrial city of Homs when security forces fired at crowds.
# Hypothesis: Clashes are reported in western city of Homs ; at least 11 are dead there.
# Golden Label: entailment

people_died_premise = 11
people_died_hypothesis = 11

# the hypothesis mentions the number of people who died in Homs, which is also referenced in the premise
if people_died_hypothesis != people_died_premise:
    # check if the number of people dead in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of people dead from the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

