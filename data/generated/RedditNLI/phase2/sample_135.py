# Premise: FDIC Says Banks on `Problem List' Rose 30% in Second Quarter.
# Hypothesis: FDIC says 117 banks on problem list in Q2, vs 90 in Q1.
# Golden Label: entailment

banks_on_problem_list_Q1 = 90
banks_on_problem_list_Q2 = 117

# Calculate the percentage increase from Q1 to Q2
percentage_increase = ((banks_on_problem_list_Q2 - banks_on_problem_list_Q1) / banks_on_problem_list_Q1) * 100

# The premise and hypothesis both mention the number of banks on the problem list in Q2
# The premise also mentions a percentage increase, which can be calculated from the numbers in the hypothesis
if percentage_increase != 30:
    # Check if the calculated percentage increase contradicts the percentage increase in the premise
    label = "contradiction"
else:
    # If the calculated percentage increase matches the percentage increase in the premise, it is an entailment
    label = "entailment"

print(label)

