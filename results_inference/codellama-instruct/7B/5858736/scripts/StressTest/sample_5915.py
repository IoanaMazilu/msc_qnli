# Define variables for the numerical entities in the premise and hypothesis
premise_score = 90
premise_tests = 3
premise_total_tests = 4

hypothesis_score = 90
hypothesis_tests = 3
hypothesis_total_tests = 4

# Extract all quantities as valid numbers
premise_score = float(premise_score)
premise_tests = int(premise_tests)
premise_total_tests = int(premise_total_tests)
hypothesis_score = float(hypothesis_score)
hypothesis_tests = int(hypothesis_tests)
hypothesis_total_tests = int(hypothesis_total_tests)

# Use brief comments to explain what comparison you do between the defined variables
if premise_score == hypothesis_score:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif premise_tests < hypothesis_tests:
    # Check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
elif premise_total_tests < hypothesis_total_tests:
    # Check if the total number of tests in the hypothesis contradicts the total number of tests reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
