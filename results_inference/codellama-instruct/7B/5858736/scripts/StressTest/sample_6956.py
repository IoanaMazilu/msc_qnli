shirts_salman_premise = 40
shirts_salman_hypothesis = 40
shirts_ambani_premise = 40
shirts_ambani_hypothesis = 40
shirts_dalmiya_premise = 40
shirts_dalmiya_hypothesis = 40

# the hypothesis talks about the average number of shirts with Salman, Ambani and Dalmiya
if shirts_salman_hypothesis >= shirts_salman_premise:
    # check if the hypothesis value contradicts the estimate of more than'shirts_salman_premise'
    label = "contradiction"
elif shirts_ambani_hypothesis >= shirts_ambani_premise:
    # check if the hypothesis value contradicts the estimate of more than'shirts_ambani_premise'
    label = "contradiction"
elif shirts_dalmiya_hypothesis >= shirts_dalmiya_premise:
    # check if the hypothesis value contradicts the estimate of more than'shirts_dalmiya_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts
    # any number of shirts less than'shirts_salman_premise','shirts_ambani_premise' and'shirts_dalmiya_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
