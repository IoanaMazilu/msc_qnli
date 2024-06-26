north_america_passengers_premise = 4/12
north_america_passengers_hypothesis = 1/12
european_passengers_premise = 1/8
european_passengers_hypothesis = 1/8
african_passengers_premise = 1/3
african_passengers_hypothesis = 1/3
asian_passengers_premise = 1/6
asian_passengers_hypothesis = 1/6
other_continent_passengers_premise = 35
other_continent_passengers_hypothesis = 35

# the hypothesis talks about the number of passengers from different continents on a ship, referenced also in the premise
if north_america_passengers_hypothesis > north_america_passengers_premise:
    # check if the number of North American passengers in the hypothesis contradicts the number of North American passengers in the premise
    label = "contradiction"
elif european_passengers_hypothesis!= european_passengers_premise:
    # check if the number of European passengers in the hypothesis contradicts the number of European passengers in the premise
    label = "contradiction"
elif african_passengers_hypothesis!= african_passengers_premise:
    # check if the number of African passengers in the hypothesis contradicts the number of African passengers in the premise
    label = "contradiction"
elif asian_passengers_hypothesis!= asian_passengers_premise:
    # check if the number of Asian passengers in the hypothesis contradicts the number of Asian passengers in the premise
    label = "contradiction"
elif other_continent_passengers_hypothesis!= other_continent_passengers_premise:
    # check if the number of passengers from other continents in the hypothesis contradicts the number of passengers from other continents in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
