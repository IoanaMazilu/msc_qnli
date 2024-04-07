# Premise: Martin has to secure 80% marks to clear his exam of class 9 th. He got 200 marks and failed by 200 marks. What is the maximum marks?
# Hypothesis: Martin has to secure 70% marks to clear his exam of class 9 th. He got 200 marks and failed by 200 marks. What is the maximum marks?
# Golden Label: contradiction

pass_percentage_premise = 80
marks_got_premise = 200
marks_failed_premise = 200

pass_percentage_hypothesis = 70
marks_got_hypothesis = 200
marks_failed_hypothesis = 200

# the hypothesis refers to the pass percentage, marks got, and marks failed by Martin
if pass_percentage_premise != pass_percentage_hypothesis:
    # check if the pass percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif marks_got_hypothesis != marks_got_premise or marks_failed_hypothesis != marks_failed_premise:
    # check if the marks got or marks failed by Martin in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

