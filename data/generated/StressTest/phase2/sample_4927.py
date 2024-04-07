# Premise: If less than 8/3 of the passengers on a ship are from North America, 1/8 are Europeans, 1/5 are from Africa, 1/6 are from Asia and the remaining 42 people are citizens of other continents, then how many passengers are on board the ship?
# Hypothesis: If 1/3 of the passengers on a ship are from North America, 1/8 are Europeans, 1/5 are from Africa, 1/6 are from Asia and the remaining 42 people are citizens of other continents, then how many passengers are on board the ship?
# Golden Label: neutral

north_america_passengers_premise = 8/3
north_america_passengers_hypothesis = 1/3
european_passengers = 1/8
african_passengers = 1/5
asian_passengers = 1/6
other_passengers = 42

# the hypothesis talks about the number of passengers from different continents on a ship, referenced also in the premise
if north_america_passengers_hypothesis >= north_america_passengers_premise:
    # check if the hypothesis value contradicts the estimate of less than 'north_america_passengers_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of north american passengers
    # any number of north american passengers less than 'north_america_passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

