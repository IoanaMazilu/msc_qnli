miles_premise = 200
miles_hypothesis = 300

# the hypothesis talks about the number of miles traveled by Louisa on the first day of her vacation
if miles_hypothesis <= miles_premise:
    # check if the hypothesis value contradicts the estimate of more than'miles_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of miles traveled
    # any number of miles greater than'miles_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
