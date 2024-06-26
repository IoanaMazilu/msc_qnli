percentage_increase_premise = 30
banks_problem_list_hypothesis_q2 = 117
banks_problem_list_premise_q2 = 30  # This is the percentage increase in banks on the problem list in the second quarter according to the premise
banks_problem_list_hypothesis_q1 = 90

# The hypothesis and premise both mention the number of banks on the problem list
# However, the hypothesis provides specific numbers for Q2 and Q1, while the premise only provides a percentage increase in Q2
if banks_problem_list_hypothesis_q2!= banks_problem_list_premise_q2:
    # Check if the number of banks on the problem list in Q2 according to the hypothesis contradicts the percentage increase in Q2 according to the premise
    label = "contradiction"
elif banks_problem_list_hypothesis_q1!= banks_problem_list_premise_q2:
    # Check if the number of banks on the problem list in Q1 according to the hypothesis contradicts the percentage increase in Q2 according to the premise
    label = "contradiction"
else:
    # The premise only provides a percentage increase in Q2, so any number for Q1 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
