north_america_premise = 4/12
north_america_hypothesis = 1/12
europe_premise = 1/8
europe_hypothesis = 1/8
africa_premise = 1/3
africa_hypothesis = 1/3
asia_premise = 1/6
asia_hypothesis = 1/6
other_continents_premise = 35
other_continents_hypothesis = 35

# the hypothesis talks about the number of passengers from each continent, referenced also in the premise
if north_america_hypothesis >= north_america_premise:
    # check if the hypothesis value contradicts the estimate of less than 'north_america_premise'
    label = "contradiction"
elif europe_hypothesis!= europe_premise:
    # check if the number of passengers from Europe in the hypothesis contradicts the number of passengers from Europe reported in the premise
    label = "contradiction"
elif africa_hypothesis!= africa_premise:
    # check if the number of passengers from Africa in the hypothesis contradicts the number of passengers from Africa reported in the premise
    label = "contradiction"
elif asia_hypothesis!= asia_premise:
    # check if the number of passengers from Asia in the hypothesis contradicts the number of passengers from Asia reported in the premise
    label = "contradiction"
elif other_continents_hypothesis!= other_continents_premise:
    # check if the number of passengers from other continents in the hypothesis contradicts the number of passengers from other continents reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers from North America
    # any number of passengers from North America less than 'north_america_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
