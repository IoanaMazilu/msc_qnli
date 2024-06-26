# the premise and hypothesis are about the distribution of passengers by continent
# the premise specifies the number of passengers from each continent,
# the hypothesis specifies the number of passengers from each continent

# compute the number of passengers from North America in the premise and hypothesis
n_passengers_north_america_premise = 1/12
n_passengers_north_america_hypothesis = 4/12
if n_passengers_north_america_premise >= n_passengers_north_america_hypothesis:
    # check if the number of passengers from North America in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of passengers from North America in the hypothesis is less than in the premise, we can infer entailment
    label = "entailment"

print(label)
