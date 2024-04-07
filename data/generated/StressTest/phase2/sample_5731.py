# Premise: If the marks secured by Reema was written as less than 76 instead of 96 then find the correct average marks up to two decimal places.
# Hypothesis: If the marks secured by Reema was written as 46 instead of 96 then find the correct average marks up to two decimal places.
# Golden Label: neutral

reema_marks_premise = 76
reema_marks_hypothesis = 46

# the hypothesis refers to a possible error in Reema's marks mentioned in the premise
if reema_marks_hypothesis != reema_marks_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

