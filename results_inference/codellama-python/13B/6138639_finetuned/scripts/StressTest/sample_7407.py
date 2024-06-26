letters_tuesday_premise = 7
letters_tuesday_hypothesis = 4
letters_wednesday_premise = 3
letters_wednesday_hypothesis = 3

# the hypothesis refers to the number of letters written by Sam on Tuesday and Wednesday, mentioned in the premise
if letters_tuesday_premise <= letters_tuesday_hypothesis:
    # check if the estimate of 'letters_tuesday_hypothesis' contradicts the number of letters written on Tuesday in the premise
    label = "contradiction"
elif letters_wednesday_hypothesis!= letters_wednesday_premise:
    # check if the number of letters written on Wednesday in the hypothesis contradicts the number of letters written on Wednesday reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
