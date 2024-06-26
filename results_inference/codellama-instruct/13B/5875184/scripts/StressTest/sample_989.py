seniors_premise = 300
seniors_hypothesis = 300
cars_premise = 0.5
cars_hypothesis = 0.5

# the hypothesis refers to the number of seniors and the percentage of them with cars
if seniors_hypothesis > seniors_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif cars_hypothesis > cars_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an estimate for the number of seniors and the percentage of them with cars
    # any number of seniors greater than'seniors_premise' and any percentage of them with cars greater than 'cars_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
