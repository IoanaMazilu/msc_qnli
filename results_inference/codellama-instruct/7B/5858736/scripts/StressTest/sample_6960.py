# Define variables for the premise and hypothesis
test_score_premise = 60
num_tests_premise = 4
test_score_hypothesis = 60
num_tests_hypothesis = 2

# Check if the hypothesis value contradicts the premise value
if test_score_hypothesis!= test_score_premise:
    label = "contradiction"
# Check if the number of tests in the hypothesis contradicts the number of tests in the premise
elif num_tests_hypothesis!= num_tests_premise:
    label = "contradiction"
# If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
else:
    label = "entailment"

print(label)
