# Premise: If the marks secured by Reema was written as less than 60 instead of 85 then find the correct average marks up to two decimal places.
# Hypothesis: If the marks secured by Reema was written as 50 instead of 85 then find the correct average marks up to two decimal places.
# Golden Label: neutral

marks_premise = 60
marks_hypothesis = 50
actual_marks = 85

# the hypothesis refers to the marks of Reema mentioned in the premise
if marks_hypothesis >= marks_premise:
    # check if the hypothesis value contradicts the premise's statement of Reema's marks being less than 'marks_premise'
    label = "contradiction"
elif marks_hypothesis == actual_marks:
    # Check if the marks in the hypothesis are the same as the actual marks
    label = "entailment"
else:
    # the premise gives an estimate of Reema's marks being less than 'marks_premise'
    # any actual marks greater than 'marks_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

