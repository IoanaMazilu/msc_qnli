# Premise: At least five people were transported to a local hospital, Red Cross said on its Twitter page.
# Hypothesis: At least five people are taken to a local hospital.
# Golden Label: entailment

people_premise = 5
people_hypothesis = 5

# the hypothesis mentions the number of people taken to a local hospital, which is also referenced in the premise
if people_hypothesis < people_premise:
    # check if the number of people in the hypothesis is less than the number reported in the premise
    label = "contradiction"
else:
    # if the number of people in the hypothesis is not less than the number in the premise, we can infer entailment
    label = "entailment"

print(label)

