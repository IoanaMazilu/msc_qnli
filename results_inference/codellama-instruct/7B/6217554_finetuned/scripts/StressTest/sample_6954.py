average_shirts_premise = 40
average_shirts_hypothesis = 80

# the hypothesis gives an estimate for the average number of shirts
# any number of shirts greater than 'average_shirts_hypothesis' contradicts the premise
if average_shirts_hypothesis <= average_shirts_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the average number of shirts
    # any number of shirts greater than 'average_shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
