# Define variables for the numerical entities in the premise and hypothesis
premise_score = 78
premise_tests = 3
hypothesis_score = 78
hypothesis_tests = 6

# Extract all quantities as valid numbers
premise_score = float(premise_score)
premise_tests = int(premise_tests)
hypothesis_score = float(hypothesis_score)
hypothesis_tests = int(hypothesis_tests)

# Use brief comments to explain what comparison you do between the defined variables
if hypothesis_score <= premise_score:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif hypothesis_tests <= premise_tests:
    # Check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
