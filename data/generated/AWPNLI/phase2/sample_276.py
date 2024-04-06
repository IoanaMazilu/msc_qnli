# Premise: A teacher had 6.0 worksheets to grade, and she graded 4.0 but then another 18.0 were turned in.
# Hypothesis: She would have 20.0 worksheets to grade.
# Golden Label: entailment

initial_worksheets_premise = 6.0
graded_worksheets_premise = 4.0
turned_in_worksheets_premise = 18.0
total_worksheets_hypothesis = 20.0

# the hypothesis refers to the total number of worksheets, which is also mentioned in the premise
# compute the total number of worksheets in the premise
total_worksheets_premise = initial_worksheets_premise - graded_worksheets_premise + turned_in_worksheets_premise
if total_worksheets_hypothesis != total_worksheets_premise:
    # check if the number of worksheets in the hypothesis contradicts the number of worksheets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

