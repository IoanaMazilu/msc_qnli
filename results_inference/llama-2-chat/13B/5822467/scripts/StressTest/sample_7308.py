minutes_to_type_premise = 4
words_to_type_premise = 8
rate_of_typing_premise = 4

# the hypothesis refers to the number of words typed and the rate of typing mentioned in the premise
if words_to_type_hypothesis > words_to_type_premise:
    # check if the hypothesis value contradicts the estimate of 'words_to_type_premise'
    label = "contradiction"
elif minutes_to_type_hypothesis!= minutes_to_type_premise:
    # check if the number of minutes to type more than 7 words in the hypothesis contradicts the number of minutes to type 8 words in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
