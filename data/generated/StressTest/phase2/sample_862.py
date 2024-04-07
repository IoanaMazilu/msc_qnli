# Premise: Dawson has to secure more than 20% marks to clear his exam of class 8 th. He got 30 marks and failed by 36 marks. What is the maximum marks?
# Hypothesis: Dawson has to secure 30% marks to clear his exam of class 8 th. He got 30 marks and failed by 36 marks. What is the maximum marks?
# Golden Label: neutral

percentage_premise = 20
percentage_hypothesis = 30
marks_obtained = 30
marks_failed_by = 36

# the hypothesis refers to the percentage of marks needed to pass the exam, which is also mentioned in the premise
if percentage_hypothesis <= percentage_premise:
    # check if the percentage value in the hypothesis contradicts the estimate of more than 'percentage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of marks needed to pass
    # a higher percentage needed to pass is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

