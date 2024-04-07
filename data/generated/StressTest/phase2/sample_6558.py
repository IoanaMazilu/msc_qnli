# Premise: Jerry’s average (arithmetic mean) score on the first 3 of 4 tests is 78.
# Hypothesis: Jerry’s average (arithmetic mean) score on the first less than 6 of 4 tests is 78.
# Golden Label: entailment

tests_count_premise = 3
tests_count_hypothesis = 6 # less than 6 is still greater than 3
score_premise = 78
score_hypothesis = 78

# Both hypothesis and premise talk about Jerry's average score on a number of tests
if tests_count_hypothesis < tests_count_premise:
    # Check if the number of tests mentioned in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif score_hypothesis != score_premise:
    # Check if the average score mentioned in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

