gang_premise = 3
gang_hypothesis = 7

# the hypothesis refers to the number of gang members in a friendship gang
# any number of gang members greater than or equal to the number of gang members in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
if gang_hypothesis >= gang_premise:
    label = "neutral"
else:
    label = "contradiction"

print(label)
