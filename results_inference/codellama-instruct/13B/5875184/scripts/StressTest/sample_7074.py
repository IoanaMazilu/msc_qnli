premise_rank = 65
hypothesis_rank = 15
class_size = 182

# the hypothesis refers to the rank of Veena in a class of 182
if hypothesis_rank <= premise_rank:
    # check if the estimate of 'hypothesis_rank' contradicts the rank of Veena in the premise
    label = "contradiction"
elif hypothesis_rank > premise_rank:
    # check if the rank of Veena in the hypothesis is consistent with the premise
    if hypothesis_rank > class_size:
        # check if the rank of Veena in the hypothesis is greater than the class size
        label = "contradiction"
    else:
        # the premise gives only an estimate for the rank of Veena
        # any rank greater than 'premise_rank' is consistent with the premise, but cannot be explicitly entailed from the premise
        label = "neutral"
else:
    # the premise gives only an estimate for the rank of Veena
    # any rank greater than 'premise_rank' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
