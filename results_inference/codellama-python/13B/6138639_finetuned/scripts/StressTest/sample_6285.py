test_score_premise = 83
test_score_hypothesis = 83
test_average_premise = 10
test_average_hypothesis = 70

# the hypothesis talks about the score and average score of Robin, referenced also in the premise
if test_score_hypothesis!= test_score_premise:
    # check if the test score in the hypothesis contradicts the test score reported in the premise
    label = "contradiction"
elif test_average_hypothesis <= test_average_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # the premise gives the average score and the test score
    # any test score less than 'test_score_premise' and average score less than 'test_average_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
