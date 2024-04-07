# Premise: Henry has to secure more than 30% marks to clear his exam of class 6 th. He got 110 marks and failed by 100 marks. What is the maximum marks?
# Hypothesis: Henry has to secure 70% marks to clear his exam of class 6 th. He got 110 marks and failed by 100 marks. What is the maximum marks?
# Golden Label: neutral

percentage_to_clear_premise = 30
percentage_to_clear_hypothesis = 70
marks_got = 110
marks_failed_by = 100

# the hypothesis refers to the percentage of marks needed to clear the exam and the marks got by Henry, which are both mentioned in the premise
if percentage_to_clear_hypothesis <= percentage_to_clear_premise:
    # check if the 'percentage_to_clear_hypothesis' contradicts the 'percentage_to_clear_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of marks needed to clear the exam
    # any percentage of marks greater than 'percentage_to_clear_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

