# Premise: Each week, Harry is paid x dollars per hour for the first 30 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first more than 30 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: contradiction

standard_hours_premise = 30
standard_hours_hypothesis = 30

# the hypothesis refers to the number of standard paid hours mentioned in the premise
if standard_hours_hypothesis > standard_hours_premise:
    # check if the hypothesis value contradicts the number of standard paid hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

