# Premise: If 1/12 of the passengers on a ship are from North America, 1/4 are Europeans, 1/9 are from Africa, 1/6 are from Asia and the remaining 42 people are citizens of other continents, then how many passengers are on board the ship?
# Hypothesis: If less than 1/12 of the passengers on a ship are from North America, 1/4 are Europeans, 1/9 are from Africa, 1/6 are from Asia and the remaining 42 people are citizens of other continents, then how many passengers are on board the ship?
# Golden Label: contradiction

# fractions of passengers from different continents in the premise
na_fraction_premise = 1/12
eu_fraction_premise = 1/4
af_fraction_premise = 1/9
as_fraction_premise = 1/6
other_passengers_premise = 42

# fractions of passengers from different continents in the hypothesis
na_fraction_hypothesis = 1/12
eu_fraction_hypothesis = 1/4
af_fraction_hypothesis = 1/9
as_fraction_hypothesis = 1/6
other_passengers_hypothesis = 42

# the hypothesis refers to the same passengers fractions as in the premise
if na_fraction_hypothesis > na_fraction_premise:
    # check if the 'na_fraction_hypothesis' contradicts the 'na_fraction_premise'
    label = "contradiction"
elif eu_fraction_hypothesis != eu_fraction_premise or af_fraction_hypothesis != af_fraction_premise or as_fraction_hypothesis != as_fraction_premise or other_passengers_hypothesis != other_passengers_premise:
    # check if the other fractions and other passengers number in the hypothesis contradict the ones in the premise
    label = "contradiction"
else:
    # if the hypothesis fractions and numbers do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

