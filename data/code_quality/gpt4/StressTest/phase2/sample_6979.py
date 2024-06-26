directors_premise = 4
directors_hypothesis = 8

# the hypothesis refers to the number of persons serving on the board of directors of the charities mentioned in the premise
if directors_hypothesis <= directors_premise:
    # check if the hypothesis value contradicts the estimate of more than 'directors_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of directors
    # any number of directors greater than 'directors_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
