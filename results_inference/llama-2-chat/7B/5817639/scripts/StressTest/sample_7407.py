letters_tuesday_premise = 7
letters_tuesday_hypothesis = 4
letters_wednesday_premise = 3
letters_wednesday_hypothesis = 3

# the hypothesis talks about the number of letters written on Tuesday and Wednesday, referenced also in the premise
if letters_tuesday_hypothesis <= letters_tuesday_premise:
    # check if the hypothesis value contradicts the estimate of more than 'letters_tuesday_premise'
    label = "contradiction"
elif letters_wednesday_hypothesis!= letters_wednesday_premise:
    # check if the number of letters in the hypothesis contradicts the number of letters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
