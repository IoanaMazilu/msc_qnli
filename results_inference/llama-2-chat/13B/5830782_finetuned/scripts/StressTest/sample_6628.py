score1_premise = 8
score2_premise = 2
score3_premise = 3

score1_hypothesis = 1
score2_hypothesis = 2
score3_hypothesis = 3

# the hypothesis talks about the scores Mary got in a game, referenced also in the premise
if score1_hypothesis >= score1_premise or score2_hypothesis >= score2_premise or score3_hypothesis >= score3_premise:
    # check if the hypothesis value contradicts the estimate of less than'score1_premise' or'score2_premise' or'score3_premise'
    label = "contradiction"
elif score1_hypothesis == score2_hypothesis or score2_hypothesis == score3_hypothesis or score3_hypothesis == score1_hypothesis:
    # check if the hypothesis value contradicts the condition of never getting the same score in consecutive steps
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any score less than'score1_premise' and'score2_premise' and'score3_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
