# Premise: If 1/4 of the passengers on a ship are from North America, 1/8 are Europeans, 1/12 are from Africa, 1/6 are from Asia and the remaining 36 people are citizens of other continents, then how many passengers are on board the ship?
# Hypothesis: If 6/4 of the passengers on a ship are from North America, 1/8 are Europeans, 1/12 are from Africa, 1/6 are from Asia and the remaining 36 people are citizens of other continents, then how many passengers are on board the ship?
# Golden Label: contradiction

north_america_passengers_premise = 1/4
north_america_passengers_hypothesis = 6/4
europe_passengers = 1/8
africa_passengers = 1/12
asia_passengers = 1/6
other_passengers = 36

# the hypothesis refers to the same groups of passengers mentioned in the premise
# but changes the fraction of North American passengers
# we calculate the total fractions of passengers in premise and hypothesis
total_passengers_premise = north_america_passengers_premise + europe_passengers + africa_passengers + asia_passengers
total_passengers_hypothesis = north_america_passengers_hypothesis + europe_passengers + africa_passengers + asia_passengers

# if the total fractions of passengers in the hypothesis is not equal to the one in the premise
# then the hypothesis contradicts the premise
if total_passengers_premise != total_passengers_hypothesis:
    label = "contradiction"
else:
    # if North American passengers fraction in hypothesis is not equal to the one in the premise
    # then the hypothesis contradicts the premise
    if north_america_passengers_premise != north_america_passengers_hypothesis:
        label = "contradiction"
    else:
        # if the fractions are the same in the premise and hypothesis,
        # and the number of other passengers is also the same,
        # then the hypothesis can be entailed from the premise
        label = "entailment"

print(label)

