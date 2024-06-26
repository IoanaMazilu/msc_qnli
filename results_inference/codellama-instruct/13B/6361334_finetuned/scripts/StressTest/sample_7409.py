letters_tuesday_premise = 7
letters_wednesday_premise = 3
letters_tuesday_hypothesis = 3
letters_wednesday_hypothesis = 3

# the hypothesis refers to the number of letters written by Sam on Tuesday and Wednesday, which are also mentioned in the premise
if letters_tuesday_hypothesis!= letters_tuesday_premise or letters_wednesday_hypothesis!= letters_wednesday_premise:
    # check if the number of letters written by Sam on Tuesday and Wednesday in the hypothesis contradicts the number of letters written in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
