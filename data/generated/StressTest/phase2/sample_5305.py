# Premise: Min (a, b, c) = min of a, b, c Max (a, b, c,) = max of a, b, c then what is the value of MAX { min (less than 6, 5,7), max (-7,-2,-3), 3 }.
# Hypothesis: Min (a, b, c) = min of a, b, c Max (a, b, c,) = max of a, b, c then what is the value of MAX { min (2, 5,7), max (-7,-2,-3), 3 }.
# Golden Label: neutral

# Define the variables
min_a_premise = 6
min_b_premise = 5
min_c_premise = 7

max_a_premise = -7
max_b_premise = -2
max_c_premise = -3

value_premise = 3

min_a_hypothesis = 2
min_b_hypothesis = 5
min_c_hypothesis = 7

max_a_hypothesis = -7
max_b_hypothesis = -2
max_c_hypothesis = -3

value_hypothesis = 3

# Calculate the result of the expressions in the premise and hypothesis
result_premise = max(min(min_a_premise, min_b_premise, min_c_premise), max(max_a_premise, max_b_premise, max_c_premise), value_premise)
result_hypothesis = max(min(min_a_hypothesis, min_b_hypothesis, min_c_hypothesis), max(max_a_hypothesis, max_b_hypothesis, max_c_hypothesis), value_hypothesis)

# Compare the results
if result_premise == result_hypothesis:
    # If the results are equal, then the hypothesis is a entailment of the premise
    label = "entailment"
elif result_premise != result_hypothesis:
    # If the results are different, then the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the results are not equal and not different, then the relation is neutral
    label = "neutral"

print(label)

