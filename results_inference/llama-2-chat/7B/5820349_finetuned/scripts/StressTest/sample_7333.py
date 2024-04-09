samsung_phone_users_premise = 25
samsung_phone_users_hypothesis = 75
iphone_users_premise = 70
iphone_users_hypothesis = 70
samsung_phone_users_percentage_difference = samsung_phone_users_hypothesis - samsung_phone_users_premise
iphone_users_percentage_difference = iphone_users_hypothesis - iphone_users_premise

# the hypothesis refers to the percentage of Samsung and iPhone users in the same company
# it also refers to the percentage of Samsung phone users in the company after a certain percentage
# the premise and hypothesis are comparing the percentage of Samsung phone users and iPhone users in the same company
if samsung_phone_users_hypothesis <= samsung_phone_users_premise:
    # check if the percentage of Samsung phone users in the hypothesis contradicts the premise
    label = "contradiction"
elif iphone_users_hypothesis!= iphone_users_premise:
    # check if the percentage of iPhone users in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of Samsung phone users
    # any percentage of Samsung phone users greater than'samsung_phone_users_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
