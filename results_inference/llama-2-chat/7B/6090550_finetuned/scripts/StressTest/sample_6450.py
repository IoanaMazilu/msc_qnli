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

# the hypothesis refers to the same proportions of passengers as the premise
if north_america_hypothesis <= north_america_premise or europe_hypothesis!= europe_premise or africa_hypothesis!= africa_premise or asia_hypothesis!= asia_premise or other_continents_hypothesis!= other_continents_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
