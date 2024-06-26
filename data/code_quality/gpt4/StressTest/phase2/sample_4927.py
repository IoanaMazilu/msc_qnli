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
