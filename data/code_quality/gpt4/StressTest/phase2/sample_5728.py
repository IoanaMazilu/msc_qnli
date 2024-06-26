questions_solved_premise = 51
questions_solved_hypothesis = 41
questions_correct_premise = 37
questions_correct_hypothesis = 37
remaining_questions_solved_premise = 8
remaining_questions_solved_hypothesis = 8
remaining_questions_correct_premise = 5
remaining_questions_correct_hypothesis = 5

# the hypothesis talks about the number of questions solved and correct by Rajesh, also referenced in the premise
if questions_solved_hypothesis >= questions_solved_premise:
    # check if the number of questions solved in the hypothesis contradicts the estimate of less than 'questions_solved_premise'
    label = "contradiction"
elif questions_correct_hypothesis != questions_correct_premise:
    # check if the number of correct questions in the hypothesis contradicts the number of correct questions in the premise
    label = "contradiction"
elif remaining_questions_solved_hypothesis != remaining_questions_solved_premise:
    # check if the number of remaining questions solved in the hypothesis contradicts the number of remaining questions solved in the premise
    label = "contradiction"
elif remaining_questions_correct_hypothesis != remaining_questions_correct_premise:
    # check if the number of remaining questions correct in the hypothesis contradicts the number of remaining questions correct in the premise
    label = "contradiction"
elif questions_solved_hypothesis < questions_solved_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment, unless the hypothesis has a smaller number of questions solved
    label = "entailment"
else:
    # if no contradiction or entailment, the relation is neutral
    label = "neutral"

print(label)
