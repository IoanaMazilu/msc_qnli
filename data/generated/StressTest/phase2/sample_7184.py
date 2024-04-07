# Premise: If 1/12 of the passengers on a ship are from North America, 1/8 are Europeans, 1/3 are from Africa, 1/6 are from Asia and the remaining 35 people are citizens of other continents, then how many passengers are on board the ship?
# Hypothesis: If 3/12 of the passengers on a ship are from North America, 1/8 are Europeans, 1/3 are from Africa, 1/6 are from Asia and the remaining 35 people are citizens of other continents, then how many passengers are on board the ship?
# Golden Label: contradiction

na_premise = 1/12
na_hypothesis = 3/12
eu_premise = 1/8
eu_hypothesis = 1/8
af_premise = 1/3
af_hypothesis = 1/3
as_premise = 1/6
as_hypothesis = 1/6
other_premise = 35
other_hypothesis = 35

# the hypothesis refers to the number of passengers on the ship from different continents
# we need to check if the proportions in the hypothesis contradict the proportions in the premise
if na_hypothesis != na_premise or eu_hypothesis != eu_premise or af_hypothesis != af_premise or as_hypothesis != as_premise:
    label = "contradiction"
elif other_hypothesis != other_premise:
    # check if the number of passengers from other continents in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and proportions do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

