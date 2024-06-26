chocolates_premise = 55
chocolates_hypothesis = 15

# The hypothesis refers to the number of chocolates Zada has to distribute, which is also mentioned in the premise
if chocolates_hypothesis >= chocolates_premise:
    # Check if the number of chocolates in the hypothesis contradicts the 'less than' estimate in the premise
    label = "contradiction"
else:
    # Any number of chocolates less than 'chocolates_premise' is consistent with the premise, but it can't be explicitly entailed from the premise
    label = "neutral"

print(label)
