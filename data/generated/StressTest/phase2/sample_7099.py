# Premise: If the marks secured by Reema was written as less than 86 instead of 66 then find the correct average marks up to two decimal places.
# Hypothesis: If the marks secured by Reema was written as 36 instead of 66 then find the correct average marks up to two decimal places.
# Golden Label: neutral

reema_marks_premise = 86
reema_marks_hypothesis = 36

# the hypothesis talks about the marks secured by Reema, also mentioned in the premise
if reema_marks_hypothesis == reema_marks_premise:
    # check if the marks secured by Reema in the hypothesis match the marks mentioned in the premise
    label = "entailment"
elif reema_marks_hypothesis > reema_marks_premise:
    # check if the marks secured by Reema in the hypothesis contradict the marks mentioned in the premise
    label = "contradiction"
else:
    # the marks secured by Reema in the hypothesis are less than those in the premise
    # this is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

