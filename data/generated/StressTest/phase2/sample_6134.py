# Premise: Each week, James is paid x dollars per per hour for the first 40 hours and 2 x dollars for each additional hour worked that week.
# Hypothesis: Each week, James is paid x dollars per per hour for the first less than 40 hours and 2 x dollars for each additional hour worked that week.
# Golden Label: contradiction

first_hours_premise = 40
first_hours_hypothesis = 40
additional_hours_premise = 2
additional_hours_hypothesis = 2

# the hypothesis talks about the payment per hour for the first 'first_hours_hypothesis' and for each additional hour, referenced also in the premise
if first_hours_hypothesis != first_hours_premise:
    # check if the number of first hours in the hypothesis contradicts the number of first hours reported in the premise
    label = "contradiction"
elif additional_hours_hypothesis != additional_hours_premise:
    # check if the payment for additional hours in the hypothesis contradicts the payment for additional hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

