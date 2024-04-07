# Premise: Today David, who is 40 years old, and his daughter, who is 12 years old, celebrate their birthdays.
# Hypothesis: Today David, who is less than 40 years old, and his daughter, who is 12 years old, celebrate their birthdays.
# Golden Label: contradiction

david_age_premise = 40
david_age_hypothesis = 40
daughter_age_premise = 12
daughter_age_hypothesis = 12

# the hypothesis mentions the ages of David and his daughter, also mentioned in the premise
if david_age_hypothesis > david_age_premise:
    # check if the hypothesis value contradicts the age of David in the premise
    label = "contradiction"
elif daughter_age_hypothesis != daughter_age_premise:
    # check if the age of David's daughter in the hypothesis contradicts the age of David's daughter in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "contradiction"

print(label)

