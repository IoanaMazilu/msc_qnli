shirts_salman_premise = 40
shirts_ambani_premise = 40
shirts_dalmiya_premise = 40
shirts_salman_hypothesis = 80
shirts_ambani_hypothesis = 80
shirts_dalmiya_hypothesis = 80

# the hypothesis refers to the number of shirts each person has, which is also mentioned in the premise
if shirts_salman_hypothesis <= shirts_salman_premise and shirts_ambani_hypothesis <= shirts_ambani_premise and shirts_dalmiya_hypothesis <= shirts_dalmiya_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts each person has
    # any number of shirts greater than the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
