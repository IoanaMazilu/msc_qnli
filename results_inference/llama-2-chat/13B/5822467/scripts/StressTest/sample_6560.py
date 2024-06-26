# Define variables for the numerical entities in the premise and hypothesis
average_premise = 78
num_tests_premise = 3

# Define variables for the numerical entities in the hypothesis
average_hypothesis = 78
num_tests_hypothesis = 6

# Check if the number of tests in the hypothesis contradicts the number of tests in the premise
if num_tests_hypothesis!= num_tests_premise:
    # The hypothesis contradicts the premise, so label is contradiction
    label = "contradiction"
elif average_hypothesis!= average_premise:
    # Check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
