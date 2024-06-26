average_score_premise = 82
average_score_hypothesis = 82

# the hypothesis refers to the average test score on more than 'average_score_premise' tests
if average_score_hypothesis!= average_score_premise + 9:
    # check if the average test score in the hypothesis contradicts the average test score reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests greater than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)
