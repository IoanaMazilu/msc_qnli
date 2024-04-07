# Premise: If the marks secured by Reema was written as less than 45 instead of 99 then find the correct average marks up to two decimal places.
# Hypothesis: If the marks secured by Reema was written as 35 instead of 99 then find the correct average marks up to two decimal places.
# Golden Label: neutral

reema_marks_premise = 45
reema_marks_hypothesis = 35

# the hypothesis talks about a scenario where Reema's marks were written as a certain number, which is also referenced in the premise
if reema_marks_hypothesis != reema_marks_premise:
    # check if the hypothetical marks in the hypothesis contradicts the hypothetical marks mentioned in the premise
    label = "contradiction"
else:
    # if the hypothetical marks in the hypothesis do not contradict the hypothetical marks in the premise, we can infer entailment
    label = "entailment"

print(label)

