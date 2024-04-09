amateurs_premise = 4
amateurs_hypothesis = 5

# the hypothesis talks about the number of chess amateurs playing in Villa's chess club tournament
if amplitudes_hypothesis <= amplitudes_premise:
    # check if the hypothesis value contradicts the estimate of 'amateurs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of chess amateurs
    # any number of chess amateurs greater than 'amateurs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
