average_premise = 87
average_hypothesis = 87
tests_premise = 7
tests_hypothesis = 7

# the hypothesis refers to the average and number of tests mentioned in the premise
if average_hypothesis >= average_premise:
    # check if the average in the hypothesis is less than or equal to the average in the premise
    label = "entailment"
elif tests_hypothesis != tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer contradiction
    label = "contradiction"

print(label)
