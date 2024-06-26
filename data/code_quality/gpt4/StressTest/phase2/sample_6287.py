test_number_premise = 10
test_number_hypothesis = 30
average_score_premise = 83
average_score_hypothesis = 83

# the hypothesis refers to the average score in a different number of tests
if test_number_hypothesis != test_number_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests mentioned in the premise
    label = "contradiction"
elif average_score_hypothesis != average_score_premise:
    # check if the average score in the hypothesis contradicts the average score mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict any information in the premise, it is neutral
    label = "neutral"

print(label)
