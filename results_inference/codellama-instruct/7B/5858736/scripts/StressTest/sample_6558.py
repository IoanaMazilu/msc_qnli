# Define variables for the numerical entities in the premise and hypothesis
premise_score = 78
premise_tests = 4
premise_first_tests = 3

hypothesis_score = 78
hypothesis_tests = 4
hypothesis_first_tests = 6

# Extract all quantities as valid numbers
premise_score = float(premise_score)
premise_tests = int(premise_tests)
premise_first_tests = int(premise_first_tests)

hypothesis_score = float(hypothesis_score)
hypothesis_tests = int(hypothesis_tests)
hypothesis_first_tests = int(hypothesis_first_tests)

# Perform calculations
premise_average = premise_score / premise_tests
hypothesis_average = hypothesis_score / hypothesis_tests

# Compare the averages
if hypothesis_average <= premise_average:
    # The hypothesis value contradicts the premise
    label = "contradiction"
elif hypothesis_first_tests < premise_first_tests:
    # The hypothesis talks about a smaller number of tests than the premise
    label = "contradiction"
else:
    # The hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
