rank_premise = 15
rank_hypothesis = 75
class_size_premise = 47
class_size_hypothesis = 47

# the hypothesis talks about the rank of a student in a class, referenced also in the premise
if rank_hypothesis >= rank_premise:
    # check if the hypothesis value contradicts the rank of 'rank_premise'
    label = "contradiction"
elif class_size_hypothesis!= class_size_premise:
    # check if the number of students in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
