shirts_salman_premise = 80
shirts_salman_hypothesis = 40
shirts_ambani_premise = 80
shirts_ambani_hypothesis = 40
shirts_dalmiya_premise = 80
shirts_dalmiya_hypothesis = 40

# the hypothesis talks about the average number of shirts with Salman, Ambani and Dalmiya
if shirts_salman_hypothesis <= shirts_salman_premise:
    # check if the hypothesis value contradicts the estimate of less than'shirts_salman_premise'
    label = "contradiction"
elif shirts_ambani_hypothesis <= shirts_ambani_premise:
    # check if the hypothesis value contradicts the estimate of less than'shirts_ambani_premise'
    label = "contradiction"
elif shirts_dalmiya_hypothesis <= shirts_dalmiya_premise:
    # check if the hypothesis value contradicts the estimate of less than'shirts_dalmiya_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
