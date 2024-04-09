percentage_increase_premise = 30
banks_in_problem_list_hypothesis = 117
banks_in_problem_list_q1_hypothesis = 90

# the hypothesis and premise mention the percentage increase of banks on the problem list and the actual number of banks on the problem list in Q1 and Q2
if percentage_increase_premise!= 30:
    # check if the percentage increase in the hypothesis contradicts the percentage increase in the premise
    label = "contradiction"
elif banks_in_problem_list_hypothesis!= (banks_in_problem_list_hypothesis - banks_in_problem_list_q1_hypothesis):
    # check if the number of banks on the problem list in Q2 contradicts the number of banks on the problem list in Q1 plus the number of new banks on the problem list in Q2
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
