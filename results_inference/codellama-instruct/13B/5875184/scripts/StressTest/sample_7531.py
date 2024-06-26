premise_list = ["ABC", "BCA", "CAB"]
hypothesis_list = ["ABC", "BCA", "CAB"]

# check if the hypothesis list contains all the elements of the premise list
if hypothesis_list == premise_list:
    # check if the hypothesis list contains less than 4 positive integers
    if len(hypothesis_list) < 4:
        # check if each element in the hypothesis list is a different nonzero digit
        if len(set(hypothesis_list)) == 3:
            # the hypothesis is consistent with the premise
            label = "entailment"
        else:
            # the hypothesis is not consistent with the premise
            label = "contradiction"
    else:
        # the hypothesis is not consistent with the premise
        label = "contradiction"
else:
    # the hypothesis is not consistent with the premise
    label = "contradiction"

print(label)
