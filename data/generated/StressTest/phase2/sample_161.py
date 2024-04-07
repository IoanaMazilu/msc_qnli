# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 90.
# Hypothesis: Joe’s average (arithmetic mean) test score across 2 equally weighted tests was 90.
# Golden Label: contradiction

tests_premise = 4
average_score_premise = 90
tests_hypothesis = 2
average_score_hypothesis = 90

# the premise and hypothesis refer to the average test scores of Joe

# compare the number of tests in premise and hypothesis - they should be equal for an entailment
if tests_premise != tests_hypothesis:
    label = "neutral"
elif average_score_premise != average_score_hypothesis:
    # compare the average scores in premise and hypothesis - they should be equal for an entailment
    label = "contradiction"
else:
    # if the number of tests and the average scores in both premise and hypothesis match, we can infer entailment
    label = "entailment"

print(label)

