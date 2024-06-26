lock_password_premise = 3
lock_password_hypothesis = 7

# the hypothesis refers to the number of digits in the password mentioned in the premise
if lock_password_hypothesis <= lock_password_premise:
    # check if the estimate of 'lock_password_hypothesis' contradicts the number of digits in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of digits in the password
    # any number of digits greater than 'lock_password_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
