marcella_shoes_premise = 65
marcella_shoes_hypothesis = 25

# the hypothesis refers to the number of pairs of shoes owned by Marcella
if marcella_shoes_hypothesis <= marcella_shoes_premise:
    # check if the hypothesis value contradicts the estimate of less than'marcella_shoes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of shoes owned by Marcella
    # any number of pairs of shoes less than or equal to 25 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
