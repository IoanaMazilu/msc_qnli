shoes_premise = 25
shoes_hypothesis = 25

# the hypothesis talks about the number of shoes Marcella has, referenced also in the premise
if shoes_hypothesis >= shoes_premise:
    # check if the hypothesis value contradicts the estimate of less than'shoes_premise'
    label = "contradiction"
else:
    # the premise gives the exact number of shoes Marcella has
    # any number of shoes less than'shoes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
