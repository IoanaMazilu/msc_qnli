# Premise: If the marks secured by Reema was written as 46 instead of 96 then find the correct average marks up to two decimal places.
# Hypothesis: If the marks secured by Reema was written as less than 76 instead of 96 then find the correct average marks up to two decimal places.
# Golden Label: entailment

marks_premise = 46
correct_marks_premise = 96
marks_hypothesis = 76
correct_marks_hypothesis = 96

# the hypothesis refers to Reema's marks mentioned in the premise
if marks_hypothesis < marks_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif correct_marks_hypothesis != correct_marks_premise:
    # check if the correct marks in the hypothesis contradicts the correct marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

