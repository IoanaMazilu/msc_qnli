average_score_premise = 90
average_score_hypothesis = 90
number_of_tests_premise = 3
number_of_tests_hypothesis = 3

# the hypothesis refers to the average score and the number of tests mentioned in the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif number_of_tests_hypothesis <= number_of_tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # the premise gives an explicit number of tests
    # any number of tests more than 'number_of_tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
