test_score_premise = 45
test_number_premise = 4
test_score_hypothesis = 45
test_number_hypothesis = 4  # Although the hypothesis mentions 'less than 4', we don't have a specific number, so we keep it same for now

# the hypothesis refers to the average test score and the number of tests mentioned in the premise
if test_score_hypothesis != test_score_premise:
    # check if the average test score in the hypothesis contradicts the average test score in the premise
    label = "contradiction"
elif test_number_hypothesis >= test_number_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
