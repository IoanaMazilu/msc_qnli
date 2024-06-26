average_premise = 90
num_tests_premise = 3

average_hypothesis = 90
num_tests_hypothesis = 4

# the hypothesis refers to the number of tests and the average score
if num_tests_hypothesis > num_tests_premise:
    # check if the estimate of 'average_hypothesis' contradicts the number of tests reported in the premise
    label = "contradiction"
elif average_hypothesis!= average_premise:
    # check if the estimate of 'average_hypothesis' contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
