average_shirts_premise = 40
average_shirts_hypothesis = 40
shirts_purchased_each = 8

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya
if average_shirts_hypothesis >= average_shirts_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_shirts_premise'
    label = "contradiction"
else:
    # the premise gives the initial average number of shirts each person had
    # the hypothesis gives the average number of shirts each person has after purchasing
    # we can't directly compare the two because the purchasing activity is not mentioned in the premise
    label = "neutral"

print(label)
