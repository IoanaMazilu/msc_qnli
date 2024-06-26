north_america_passengers_premise = 1/12
north_america_passengers_hypothesis = 4/12
european_passengers_premise = 1/8
european_passengers_hypothesis = 1/8
african_passengers_premise = 1/3
african_passengers_hypothesis = 1/3
asian_passengers_premise = 1/6
asian_passengers_hypothesis = 1/6
other_continent_passengers_premise = 35
other_continent_passengers_hypothesis = 35

# the hypothesis refers to the same group of passengers as the premise, but changes the proportion of passengers from North America
if north_america_passengers_hypothesis <= north_america_passengers_premise:
    # check if the hypothesis value contradicts the estimate of 'north_america_passengers_premise'
    label = "contradiction"
elif european_passengers_hypothesis!= european_passengers_premise or \
        african_passengers_hypothesis!= african_passengers_premise or \
        asian_passengers_hypothesis!= asian_passengers_premise or \
        other_continent_passengers_hypothesis!= other_continent_passengers_premise:
    # check if the number of other passengers in the hypothesis contradicts the number of other passengers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
