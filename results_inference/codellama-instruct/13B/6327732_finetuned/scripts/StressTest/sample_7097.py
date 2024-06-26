premise_rank = 15
premise_class_size = 47
hypothesis_rank = 65
hypothesis_class_size = 47

# the hypothesis refers to the rank of Nitin in a class of 47 students, mentioned in the premise
if hypothesis_rank <= premise_rank:
    # check if the estimate of 'hypothesis_rank' contradicts the rank of Nitin in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the rank of Nitin
    # any rank greater than 'premise_rank' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
