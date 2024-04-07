# Premise: If 1/12 of the passengers on a ship are from North America, 1/4 are Europeans, 1/9 are from Africa, 1/6 are from Asia and the remaining 42 people are citizens of other continents, then how many passengers are on board the ship?
# Hypothesis: If less than 5/12 of the passengers on a ship are from North America, 1/4 are Europeans, 1/9 are from Africa, 1/6 are from Asia and the remaining 42 people are citizens of other continents, then how many passengers are on board the ship?
# Golden Label: entailment

north_america_premise = 1/12
north_america_hypothesis = 5/12
europe_premise = 1/4
europe_hypothesis = 1/4
africa_premise = 1/9
africa_hypothesis = 1/9
asia_premise = 1/6
asia_hypothesis = 1/6
other_continents_premise = 42
other_continents_hypothesis = 42

# the hypothesis is about the same distribution of passengers from different continents as the premise, except for North America
if north_america_hypothesis >= north_america_premise:
    # check if the estimate of 'north_america_hypothesis' contradicts the fraction of North American passengers in the premise
    label = "contradiction"
elif europe_hypothesis != europe_premise or africa_hypothesis != africa_premise or asia_hypothesis != asia_premise or other_continents_hypothesis != other_continents_premise:
    # check if the fractions of passengers from other continents in the hypothesis contradict the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

