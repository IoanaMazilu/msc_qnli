# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 70.
# Hypothesis: Joe’s average (arithmetic mean) test score across less than 5 equally weighted tests was 70.
# Golden Label: entailment

test_count_premise = 4
test_count_hypothesis = 5
test_score_premise = 70
test_score_hypothesis = 70

# the hypothesis talks about the average test score and the number of tests, both also referenced in the premise
if test_score_hypothesis != test_score_premise:
    # check if the average test score in the hypothesis contradicts the average test score reported in the premise
    label = "contradiction"
elif test_count_hypothesis <= test_count_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

