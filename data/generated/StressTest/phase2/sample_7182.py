# Premise: If 1/12 of the passengers on a ship are from North America, 1/8 are Europeans, 1/3 are from Africa, 1/6 are from Asia and the remaining 35 people are citizens of other continents, then how many passengers are on board the ship?
# Hypothesis: If less than 4/12 of the passengers on a ship are from North America, 1/8 are Europeans, 1/3 are from Africa, 1/6 are from Asia and the remaining 35 people are citizens of other continents, then how many passengers are on board the ship?
# Golden Label: entailment

north_america_passengers_premise = 1/12
north_america_passengers_hypothesis = 4/12
other_continents_passengers = 35

# the hypothesis refers to the fraction of passengers from North America mentioned in the premise
if north_america_passengers_hypothesis <= north_america_passengers_premise:
    # check if the fraction of 'north_america_passengers_hypothesis' contradicts the fraction of passengers from North America in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are identical except for the fraction of passengers from North America
    # any fraction less than 'north_america_passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

