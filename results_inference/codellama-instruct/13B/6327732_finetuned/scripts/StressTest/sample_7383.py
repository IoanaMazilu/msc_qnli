premise_rank = 24
hypothesis_rank = 74
class_size = 58

# the hypothesis talks about the rank of Nitin in a class of 58 students, referenced also in the premise
if hypothesis_rank <= premise_rank:
    # check if the hypothesis value contradicts the rank of Nitin in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the rank of Nitin
    # any rank less than 'hypothesis_rank' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
