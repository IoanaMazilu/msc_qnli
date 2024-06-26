tests_premise = 4
tests_hypothesis = 2
average_score_premise = 60
average_score_hypothesis = 60

# The hypothesis refers to the average test score of Joe, which is also mentioned in the premise
# But the number of tests taken into account to calculate the average is different
if average_score_premise != average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif tests_premise == tests_hypothesis:
    # check if the number of tests taken into account in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # if the average score and the number of tests in the hypothesis do not contradict the premise ones, we can infer neutrality
    # because the premise does not provide information about the score of each individual test Joe took
    label = "neutral"

print(label)
