# Premise: Each week, James is paid x dollars per per hour for the first 40 hours and 2 x dollars for each additional hour worked that week.
# Hypothesis: Each week, James is paid x dollars per per hour for the first more than 40 hours and 2 x dollars for each additional hour worked that week.
# Golden Label: contradiction

hourly_rate_premise = 40
hourly_rate_hypothesis = 40

# the hypothesis refers to the number of hours for which James is paid x dollars, which is also mentioned in the premise
if hourly_rate_hypothesis != hourly_rate_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

