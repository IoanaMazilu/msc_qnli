# Premise: Today David, who is 40 years old, and his daughter, who is 12 years old, celebrate their birthdays.
# Hypothesis: Today David, who is less than 70 years old, and his daughter, who is 12 years old, celebrate their birthdays.
# Golden Label: entailment

david_age_premise = 40
david_age_hypothesis = 70
daughter_age_premise = 12
daughter_age_hypothesis = 12

# the hypothesis refers to the ages of David and his daughter mentioned in the premise
if david_age_premise >= david_age_hypothesis:
    # check if the estimate of 'david_age_hypothesis' contradicts the age of David in the premise
    label = "contradiction"
elif daughter_age_hypothesis != daughter_age_premise:
    # check if the age of David's daughter in the hypothesis contradicts the age of David's daughter reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

