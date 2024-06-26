score_premise = 83
score_hypothesis = 70

# the hypothesis refers to the score on a test that gives the average score
if score_hypothesis >= score_premise:
    # check if the estimate of'score_hypothesis' contradicts the average score in the premise
    label = "contradiction"
else:
    # any score less than'score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
