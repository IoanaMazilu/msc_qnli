score_86_premise = 86
score_75_premise = 75
score_72_premise = 72
score_63_premise = 63
score_65_premise = 65

score_86_hypothesis = 86
score_75_hypothesis = 75
score_72_hypothesis = 72
score_63_hypothesis = 63
score_65_hypothesis = 65

# the hypothesis refers to the scores mentioned in the premise
if score_86_hypothesis <= score_86_premise:
    # check if the hypothesis value contradicts the estimate of more than'score_86_premise'
    label = "contradiction"
elif score_75_hypothesis <= score_75_premise or score_72_hypothesis <= score_72_premise or score_63_hypothesis <= score_63_premise or score_65_hypothesis <= score_65_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the average mark
    # any number of scores greater than'score_86_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
