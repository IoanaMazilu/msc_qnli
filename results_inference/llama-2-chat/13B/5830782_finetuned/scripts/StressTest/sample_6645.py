north_america_passengers_premise = 1/12
north_america_passengers_hypothesis = 7/12
europe_passengers = 1/4
africa_passengers = 2/9
asia_passengers = 1/6
other_passengers = 50

# the hypothesis talks about the number of passengers from different continents on a ship, referenced also in the premise
if north_america_passengers_hypothesis < north_america_passengers_premise:
    # check if the hypothesis value contradicts the number of North American passengers in the premise
    label = "contradiction"
elif europe_passengers!= 1/4 or africa_passengers!= 2/9 or asia_passengers!= 1/6:
    # check if the number of passengers from Europe, Africa, Asia in the hypothesis contradicts the number of passengers from these continents reported in the premise
    label = "contradiction"
elif other_passengers!= 50:
    # check if the number of passengers from other continents in the hypothesis contradicts the number of passengers from other continents reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
