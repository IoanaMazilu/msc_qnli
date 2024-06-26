tuesday_letters_premise = 7
tuesday_letters_hypothesis = 3
wednesday_letters_premise = 3
wednesday_letters_hypothesis = 3

# the hypothesis refers to the number of letters Sam wrote on Tuesday and Wednesday, mentioned in the premise
if tuesday_letters_premise!= tuesday_letters_hypothesis:
    # check if the number of letters written on Tuesday in the hypothesis contradicts the number of letters written on Tuesday reported in the premise
    label = "contradiction"
elif wednesday_letters_hypothesis!= wednesday_letters_premise:
    # check if the number of letters written on Wednesday in the hypothesis contradicts the number of letters written on Wednesday reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
