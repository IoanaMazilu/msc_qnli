shirts_salman_premise = 80
shirts_ambani_premise = 80
shirts_dalmiya_premise = 80

shirts_salman_hypothesis = 40
shirts_ambani_hypothesis = 40
shirts_dalmiya_hypothesis = 40

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya
# if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them then average number of shirt each of them now has
if shirts_salman_hypothesis <= shirts_salman_premise and shirts_ambani_hypothesis <= shirts_ambani_premise and shirts_dalmiya_hypothesis <= shirts_dalmiya_premise:
    # check if the hypothesis value contradicts the estimate of less than'shirts_salman_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average number of shirts with Salman, Ambani and Dalmiya
    # any number of shirts greater than'shirts_salman_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
