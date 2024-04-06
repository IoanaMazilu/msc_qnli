# Premise: Authorities said they have committed more than 20,000 military personnel and 2.5 tons of insecticide to combat the disease.
# Hypothesis: Bolivia fights disease with 20,000-plus in military, 2.5 tons of insecticide.
# Golden Label: neutral

military_personnel_premise = 20000
military_personnel_hypothesis = 20000
insecticide_premise = 2.5
insecticide_hypothesis = 2.5

# the hypothesis mentions the number of military personnel and the amount of insecticide used to fight the disease, which are also mentioned in the premise
if military_personnel_hypothesis != military_personnel_premise:
    # check if the number of military personnel in the hypothesis contradicts the number of military personnel reported in the premise
    label = "contradiction"
elif insecticide_hypothesis != insecticide_premise:
    # check if the amount of insecticide from the hypothesis contradicts the amount of insecticide in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

