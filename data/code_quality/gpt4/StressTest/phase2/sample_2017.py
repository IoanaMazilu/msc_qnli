north_america_passengers_premise = 7/4
north_america_passengers_hypothesis = 1/4
other_continents_passengers = 36
europe_passengers = 1/8
africa_passengers = 1/12
asia_passengers = 1/6

# the hypothesis refers to the number of passengers from different continents on a ship 
# but the fraction of passengers from North America contradicts the premise
if north_america_passengers_hypothesis >= north_america_passengers_premise:
    label = "contradiction"
else:
    # we don't have the total number of passengers in the premise or the hypothesis, only fractions
    # therefore, the specific total number of passengers can't be entailed from the premise
    label = "neutral"

print(label)
