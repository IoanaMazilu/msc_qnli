# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 60.
# Hypothesis: Joe’s average (arithmetic mean) test score across more than 4 equally weighted tests was 60.
# Golden Label: contradiction

test_count_premise = 4
average_score_premise = 60
test_count_hypothesis = 4
average_score_hypothesis = 60

# The hypothesis talks about the average test score and number of tests, which is also mentioned in the premise
if test_count_hypothesis != test_count_premise:
    # Check if the number of tests in the hypothesis contradicts the number of tests mentioned in the premise
    label = "contradiction"
elif average_score_hypothesis != average_score_premise:
    # Check if the average score in the hypothesis contradicts the average score mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

