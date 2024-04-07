# Premise: Today John, who is less than 48 years old, and his daughter, who is 13 years old, celebrate their birthdays.
# Hypothesis: Today John, who is 38 years old, and his daughter, who is 13 years old, celebrate their birthdays.
# Golden Label: neutral

john_age_premise = 48
john_age_hypothesis = 38
daughter_age_premise = 13
daughter_age_hypothesis = 13

# the hypothesis specifies the ages of John and his daughter mentioned in the premise
if john_age_hypothesis >= john_age_premise:
    # check if the specified 'john_age_hypothesis' contradicts the age estimate of less than 'john_age_premise' in the premise
    label = "contradiction"
elif daughter_age_hypothesis != daughter_age_premise:
    # check if the specified 'daughter_age_hypothesis' contradicts the exact age of 'daughter_age_premise' in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

