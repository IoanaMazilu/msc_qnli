average_shirts_premise = 30
average_shirts_hypothesis = 60
shirts_purchased_each = 3

# the hypothesis talks about the average number of shirts with Salman, Ambani and Dalmiya
if average_shirts_hypothesis <= average_shirts_premise + shirts_purchased_each:
    # check if the hypothesis value contradicts the premise estimate of more than 'average_shirts_premise' 
    label = "contradiction"
elif average_shirts_hypothesis > average_shirts_premise + shirts_purchased_each:
    # if the hypothesis value is greater than the premise estimate plus the number of shirts purchased
    # it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value equals the premise estimate plus the number of shirts purchased
    # then the hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)
