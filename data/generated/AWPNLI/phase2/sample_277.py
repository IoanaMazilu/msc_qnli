# Premise: A teacher had 6.0 worksheets to grade, and she graded 4.0 but then another 18.0 were turned in.
# Hypothesis: She would have 21.0 worksheets to grade.
# Golden Label: contradiction

initial_worksheets_premise = 6.0
graded_worksheets_premise = 4.0
additional_worksheets_premise = 18.0
total_worksheets_hypothesis = 21.0

# the hypothesis refers to the total number of worksheets to grade, which are mentioned in the premise
# compute the total number of worksheets left to grade from the premise
total_worksheets_premise = initial_worksheets_premise - graded_worksheets_premise + additional_worksheets_premise
if total_worksheets_hypothesis != total_worksheets_premise:
    # check if the total worksheets in the hypothesis contradicts the number of worksheets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

