class_size_premise = 47
class_size_hypothesis = 47
rank_premise = 15
rank_hypothesis = 75

# the hypothesis talks about the rank of Nitin in a class of 47 students, referenced also in the premise
if rank_hypothesis >= rank_premise:
    # check if the hypothesis value contradicts the rank of Nitin in the premise
    label = "contradiction"
else:
    # the premise gives the rank of Nitin in a class of 47 students
    # any rank less than 'rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
