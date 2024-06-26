average_shirts_premise = 50
average_shirts_hypothesis = 60
shirts_purchased_per_person = 6

# The hypothesis refers to the average number of shirts with Salman, Ambani, and Dalmiya, as stated in the premise.
if average_shirts_hypothesis <= average_shirts_premise:
    # Check if the 'average_shirts_hypothesis' contradicts the estimate of 'average_shirts_premise'.
    label = "contradiction"
elif average_shirts_hypothesis > average_shirts_premise + shirts_purchased_per_person:
    # If the 'average_shirts_hypothesis' is greater than the sum of 'average_shirts_premise' and 'shirts_purchased_per_person',
    # it contradicts the premise that each of them purchased 6 more shirts.
    label = "contradiction"
else:
    # The premise gives an estimate for the average number of shirts before purchasing more shirts.
    # Any average number of shirts greater than 'average_shirts_premise' and less than or equal to the sum of 'average_shirts_premise' and 'shirts_purchased_per_person'
    # is consistent with the premise, but cannot be explicitly entailed from the premise.
    label = "neutral"

print(label)
