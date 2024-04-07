# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 40.
# Hypothesis: Joe’s average (arithmetic mean) test score across less than 5 equally weighted tests was 40.
# Golden Label: entailment

average_score_premise = 40
tests_premise = 4
tests_hypothesis = 5

# the hypothesis refers to the average test score and number of tests mentioned in the premise
if average_score_premise != 40:
    # check if the average test score in the hypothesis contradicts the average test score reported in the premise
    label = "contradiction"
elif tests_premise >= tests_hypothesis:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

