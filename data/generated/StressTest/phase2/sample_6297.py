# Premise: Each week, Harry is paid x dollars per hour for the first 12 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first less than 82 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: entailment

base_hours_premise = 12
base_hours_hypothesis = 82

# the hypothesis refers to the number of base hours worked by Harry, mentioned also in the premise
if base_hours_hypothesis >= base_hours_premise:
    # check if the number of 'base_hours_hypothesis' contradicts the number of base hours in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

