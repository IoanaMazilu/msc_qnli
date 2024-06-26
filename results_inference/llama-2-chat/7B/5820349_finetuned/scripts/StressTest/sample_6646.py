north_america_passengers_premise = 7/12
north_america_passengers_hypothesis = 1/12
europe_passengers = 1/4
africa_passengers = 2/9
asia_passengers = 1/6
other_passengers = 50

# the hypothesis refers to the number of passengers from different continents on a ship, as mentioned in the premise
if north_america_passengers_hypothesis >= north_america_passengers_premise:
    # check if the hypothesis value contradicts the estimate of less than 'north_america_passengers_premise'
    label = "contradiction"
elif europe_passengers!= 1/4 or africa_passengers!= 2/9 or asia_passengers!= 1/6:
    # check if the number of European, African or Asian passengers in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif other_passengers!= 50:
    # check if the number of passengers from other continents in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of North American passengers
    # any number of North American passengers less than 'north_america_passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
