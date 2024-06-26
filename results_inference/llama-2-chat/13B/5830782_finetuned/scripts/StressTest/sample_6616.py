stations_premise = 28
stations_hypothesis = 18

if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the premise of having less than'stations_premise'
    label = "contradiction"
elif stations_hypothesis < stations_premise:
    # check if the hypothesis value is less than'stations_premise'
    # if it is, then it is an entailment
    label = "entailment"

print(label)
