# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 35.
# Hypothesis: Joe’s average (arithmetic mean) test score across less than 6 equally weighted tests was 35.
# Golden Label: entailment

tests_premise = 4
tests_hypothesis = 6
average_score_premise = 35
average_score_hypothesis = 35

# the hypothesis discusses about the average score and the number of tests, mentioned also in the premise
if tests_hypothesis <= tests_premise:
    # check if the hypothesis estimate contradicts the number of tests in the premise
    label = "contradiction"
elif average_score_hypothesis != average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
