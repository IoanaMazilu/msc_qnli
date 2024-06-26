north_america_passengers_premise = 7/12
north_america_passengers_hypothesis = 1/12
european_passengers = 1/4
african_passengers = 2/9
asian_passengers = 1/6
other_passengers = 50

# the hypothesis refers to the distribution of passengers on a ship mentioned in the premise
if north_america_passengers_hypothesis >= north_america_passengers_premise:
    # check if the fraction of 'north_america_passengers_hypothesis' contradicts the fraction of North American passengers in the premise
    label = "contradiction"
elif european_passengers!= 1/4 or african_passengers!= 2/9 or asian_passengers!= 1/6:
    # check if the fractions of European, African or Asian passengers in the hypothesis contradict the fractions reported in the premise
    label = "contradiction"
elif other_passengers!= 50:
    # check if the number of passengers from other continents in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
