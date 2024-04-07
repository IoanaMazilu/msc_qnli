# Premise: If less than 5/12 of the passengers on a ship are from North America, 1/4 are Europeans, 1/9 are from Africa, 1/6 are from Asia and the remaining 42 people are citizens of other continents, then how many passengers are on board the ship?
# Hypothesis: If 1/12 of the passengers on a ship are from North America, 1/4 are Europeans, 1/9 are from Africa, 1/6 are from Asia and the remaining 42 people are citizens of other continents, then how many passengers are on board the ship?
# Golden Label: neutral

north_america_passengers_premise = 5/12
north_america_passengers_hypothesis = 1/12
europe_passengers_premise = 1/4
europe_passengers_hypothesis = 1/4
africa_passengers_premise = 1/9
africa_passengers_hypothesis = 1/9
asia_passengers_premise = 1/6
asia_passengers_hypothesis = 1/6
other_continent_passengers = 42

# The hypothesis mentions the same distribution of passengers from different continents as the premise, with exception of North America.
# We need to check whether the figures given in the hypothesis contradict the ones provided in the premise.

if north_america_passengers_hypothesis > north_america_passengers_premise:
    # Check if the number of North American passengers in the hypothesis contradicts the figure given in the premise
    label = "contradiction"
elif europe_passengers_hypothesis != europe_passengers_premise or africa_passengers_hypothesis != africa_passengers_premise or asia_passengers_hypothesis != asia_passengers_premise:
    # Check if any of the other figures in the hypothesis contradict the ones given in the premise
    label = "contradiction"
else:
    # If the figures in the hypothesis do not contradict the ones in the premise, we cannot infer entailment since the actual number of passengers is not provided
    label = "neutral"

print(label)

