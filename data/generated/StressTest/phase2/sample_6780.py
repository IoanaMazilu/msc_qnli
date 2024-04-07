# Premise: Each week, Harry is paid x dollars per hour for the first 30 hours and 2 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first less than 80 hours and 2 x dollars for each additional hour worked that week.
# Golden Label: entailment

hours_regular_pay_premise = 30
hours_regular_pay_hypothesis = 80

# the hypothesis talks about the number of hours Harry works on regular pay, referenced also in the premise
if hours_regular_pay_hypothesis != hours_regular_pay_premise:
    # check if the number of hours worked on regular pay in the hypothesis contradicts the number of hours worked on regular pay reported in the premise
    label = "contradiction"
else:
    # if the number of hours worked on regular pay in the hypothesis does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

