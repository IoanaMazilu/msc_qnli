share_difference_premise = 200
share_difference_hypothesis = 400

# the hypothesis talks about the share difference between Mani and Rani, referenced also in the premise
if share_difference_hypothesis <= share_difference_premise:
    # check if the hypothesis value contradicts the number of 'share_difference_premise'
    label = "contradiction"
elif share_difference_hypothesis > share_difference_premise:
    # the premise gives a certain value for the share difference
    # any value of the share difference greater than 'share_difference_premise' cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
