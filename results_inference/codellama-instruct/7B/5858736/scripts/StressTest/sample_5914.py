# Define variables for the numerical entities in the premise and hypothesis
premise_score = 90
premise_tests = 4
premise_first_tests = 3

hypothesis_score = 90
hypothesis_tests = 4
hypothesis_first_tests = 3

# Extract all quantities as valid numbers
premise_score = float(premise_score)
premise_tests = int(premise_tests)
premise_first_tests = int(premise_first_tests)

hypothesis_score = float(hypothesis_score)
hypothesis_tests = int(hypothesis_tests)
hypothesis_first_tests = int(hypothesis_first_tests)

# Check if the hypothesis values and estimates do not contradict the premise ones
if hypothesis_score!= premise_score:
    label = "contradiction"
elif hypothesis_tests!= premise_tests:
    label = "contradiction"
elif hypothesis_first_tests!= premise_first_tests:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
