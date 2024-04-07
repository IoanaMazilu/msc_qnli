# Premise: Martin has to secure more than 10% marks to clear his exam of class 9 th. He got 200 marks and failed by 200 marks. What is the maximum marks?
# Hypothesis: Martin has to secure 80% marks to clear his exam of class 9 th. He got 200 marks and failed by 200 marks. What is the maximum marks?
# Golden Label: neutral

marks_to_clear_premise = 10
marks_to_clear_hypothesis = 80
marks_got = 200
marks_failed_by = 200
max_marks = marks_got + marks_failed_by

# the hypothesis talks about the percentage of marks to clear the exam
# as well as the actual marks Martin got and the marks he failed by, all mentioned in the premise
if marks_to_clear_hypothesis <= marks_to_clear_premise:
    # check if the percentage of marks to clear exam in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of marks to clear the exam 
    # any percentage greater than 'marks_to_clear_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

