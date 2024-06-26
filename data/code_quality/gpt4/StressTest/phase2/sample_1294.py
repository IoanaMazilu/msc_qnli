average_shirts_premise = 10
average_shirts_hypothesis = 40
new_shirts_bought = 14

# the hypothesis refers to the average number of shirts with Salman, Ambani, and Dalmiya, referenced also in the premise
# both premise and hypothesis mention a new purchase of 'new_shirts_bought' shirts each
if average_shirts_hypothesis <= average_shirts_premise + new_shirts_bought:
    # check if the hypothesis value contradicts the estimate of more than 'average_shirts_premise'
    label = "contradiction"
elif average_shirts_hypothesis > average_shirts_premise + new_shirts_bought:
    # check if the hypothesis value is more than the sum of 'average_shirts_premise' and 'new_shirts_bought'
    label = "neutral"
else:
    # the premise gives only an estimate for the average number of shirts
    # any number of shirts greater than 'average_shirts_premise' + 'new_shirts_bought' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
