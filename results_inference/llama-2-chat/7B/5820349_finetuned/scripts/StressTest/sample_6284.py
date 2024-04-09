tests_taken_premise = 9
tests_taken_hypothesis = 9
average_score_premise = 82
average_score_hypothesis = 82

# the hypothesis refers to the average test score and the number of tests taken by Robin mentioned in the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif tests_taken_hypothesis <= tests_taken_premise:
    # check if the number of tests taken in the hypothesis contradicts the number of tests taken reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
