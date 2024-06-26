shoes_premise = 65
shoes_hypothesis = 25

# the hypothesis refers to the number of shoes Marcella has, which is also mentioned in the premise
if shoes_hypothesis >= shoes_premise:
    # check if the hypothesis value contradicts the estimate of less than'shoes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shoes
    # any number of shoes less than'shoes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
