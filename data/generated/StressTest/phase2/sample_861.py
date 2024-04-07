# Premise: Dawson has to secure 30% marks to clear his exam of class 8 th. He got 30 marks and failed by 36 marks. What is the maximum marks?
# Hypothesis: Dawson has to secure more than 20% marks to clear his exam of class 8 th. He got 30 marks and failed by 36 marks. What is the maximum marks?
# Golden Label: entailment

clearing_percentage_premise = 30
clearing_percentage_hypothesis = 20
marks_got = 30
marks_failed = 36

max_marks = marks_got + marks_failed # maximum marks is the sum of marks got and marks failed

# the hypothesis refers to the clearing percentage and marks obtained/fail mentioned in the premise
if clearing_percentage_hypothesis >= clearing_percentage_premise:
    # check if the estimate of 'clearing_percentage_hypothesis' contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

