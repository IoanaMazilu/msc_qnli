list_l_premise = ['ABC', 'BCA', 'CAB']
list_l_hypothesis = ['ABC', 'BCA', 'CAB']

# the hypothesis refers to the same list as in the premise
if len(list_l_hypothesis) <= 4:
    # check if the number of positive integers in the hypothesis contradicts the number of positive integers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
