average_shirts_premise = 80
average_shirts_hypothesis = 40
shirts_purchased = 8

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya, mentioned in the premise
if average_shirts_hypothesis >= average_shirts_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_shirts_premise'
    label = "contradiction"
elif average_shirts_hypothesis < average_shirts_premise:
    # if the hypothesis value is less than 'average_shirts_premise', it is consistent with the premise
    # but the premise does not provide any information about the exact average number of shirts after purchase
    # hence, the relation is neutral
    label = "neutral"

print(label)
