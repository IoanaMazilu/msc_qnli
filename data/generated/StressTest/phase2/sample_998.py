# Premise: Nick's average (arithmetic mean) test score on 4 tests is 78.
# Hypothesis: Nick's average (arithmetic mean) test score on 3 tests is 78.
# Golden Label: contradiction

average_score_premise = 78
tests_premise = 4
average_score_hypothesis = 78
tests_hypothesis = 3

# Hypothesis refers to the average test score of Nick mentioned in the premise but with different number of tests

# Calculate total score for both premise and hypothesis
total_score_premise = average_score_premise * tests_premise
total_score_hypothesis = average_score_hypothesis * tests_hypothesis

if total_score_hypothesis == total_score_premise:
    # Check if the total score in the hypothesis contradicts the total score in the premise
    label = "contradiction"
elif average_score_hypothesis != average_score_premise:
    # Check if the average test score in the hypothesis contradicts the average test score in the premise
    label = "contradiction"
else:
    # The premise and hypothesis have the same average test score but the number of tests conducted is not specified
    # Hence, it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

