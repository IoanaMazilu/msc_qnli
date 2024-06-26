list_l_premise = ['ABC', 'BCA', 'CAB']
list_l_hypothesis = ['ABC', 'BCA', 'CAB']

# the hypothesis talks about the number of positive integers in a list, referenced also in the premise
if len(list_l_hypothesis) <= len(list_l_premise):
    # check if the hypothesis value contradicts the estimate of less than 'len(list_l_premise)'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of positive integers
    # any number of positive integers greater than or equal to the number of positive integers in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
