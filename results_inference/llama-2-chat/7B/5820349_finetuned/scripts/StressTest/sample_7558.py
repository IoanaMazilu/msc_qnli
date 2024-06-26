shoes_marcella_premise = 65
shoes_marcella_hypothesis = 25

# the hypothesis talks about the number of shoes Marcella has, referenced also in the premise
if shoes_marcella_hypothesis >= shoes_marcella_premise:
    # check if the hypothesis value contradicts the estimate of less than'shoes_marcella_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shoes
    # any number of shoes less than'shoes_marcella_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
