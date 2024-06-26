stations_vij_chen_premise = 8
stations_vij_chen_hypothesis = 2

# the hypothesis talks about the number of stations between Vijayawada and Chennai, referenced also in the premise
if stations_vij_chen_hypothesis <= stations_vij_chen_premise:
    # check if the hypothesis value contradicts the estimate of more than'stations_vij_chen_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations greater than'stations_vij_chen_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
