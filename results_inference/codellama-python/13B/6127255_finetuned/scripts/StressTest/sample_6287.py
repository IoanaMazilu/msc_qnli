#test_count_premise = 10
#average_score_premise = 83
#test_count_hypothesis = 30
#average_score_hypothesis = 83

# the hypothesis refers to the same average score on a different number of tests
# we need to calculate Robin's score for the same average score on the same number of tests
# if the number of tests in the hypothesis is not the same as in the premise, we can't infer the score from the premise
# if the average scores are not the same, we can't infer the score from the premise

#if test_count_hypothesis!= test_count_premise or average_score_hypothesis!= average_score_premise:
#    label = "contradiction"
#else:
#    label = "neutral"

#print(label)
#