samsung_phone_premise = 25
samsung_phone_hypothesis = 75
iphone_user_premise = 70
iphone_user_hypothesis = 70
samsung_phone_condition = 85

# The hypothesis refers to the percentage of Samsung and iPhone users in the company, which is also mentioned in the premise.
# Also, a condition is given when 85% of users are using Samsung phone, but no specific information about iPhone users is provided for this condition.

# First, we compare the percentage of Samsung users in the premise and hypothesis.
if samsung_phone_hypothesis <= samsung_phone_premise:
    # If the percentage of Samsung users in the hypothesis is less than or equal to the percentage in the premise, it is a contradiction.
    label = "contradiction"
elif iphone_user_hypothesis != iphone_user_premise:
    # If the percentage of iPhone users in the hypothesis is not equal to the percentage in the premise, it is a contradiction.
    label = "contradiction"
else:
    # The premise gives an estimate (more than 25%) for the percentage of Samsung users.
    # Any percentage of Samsung users greater than 'samsung_phone_premise' is consistent with the premise, but cannot be explicitly entailed from the premise.
    label = "neutral"

print(label)
