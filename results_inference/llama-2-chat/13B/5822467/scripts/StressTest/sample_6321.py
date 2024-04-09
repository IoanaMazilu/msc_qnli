amateurs_premise = 4
amateurs_hypothesis = 8

# the hypothesis refers to the number of chess amateurs playing in the tournament
if amateurs_hypothesis <= amateurs_premise:
    # check if the hypothesis value contradicts the estimate of 'amateurs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of chess amateurs
    # any number of chess amateurs less than or equal to 'amateurs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
