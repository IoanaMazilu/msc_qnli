# Premise: Dawson has to secure 30% marks to clear his exam of class 8 th. He got 30 marks and failed by 36 marks. What is the maximum marks?
# Hypothesis: Dawson has to secure 60% marks to clear his exam of class 8 th. He got 30 marks and failed by 36 marks. What is the maximum marks?
# Golden Label: contradiction

percentage_required_premise = 30
marks_obtained_premise = 30
marks_failed_premise = 36

percentage_required_hypothesis = 60
marks_obtained_hypothesis = 30
marks_failed_hypothesis = 36

# the hypothesis refers to the required percentage, obtained marks, and failed marks in the premise
if percentage_required_premise != percentage_required_hypothesis:
    # check if the required percentage in the hypothesis contradicts the required percentage in the premise
    label = "contradiction"
elif marks_obtained_premise != marks_obtained_hypothesis:
    # check if the obtained marks in the hypothesis contradicts the obtained marks in the premise
    label = "contradiction"
elif marks_failed_premise != marks_failed_hypothesis:
    # check if the failed marks in the hypothesis contradicts the failed marks in the premise
    label = "contradiction"
else:
    # if all the values in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

