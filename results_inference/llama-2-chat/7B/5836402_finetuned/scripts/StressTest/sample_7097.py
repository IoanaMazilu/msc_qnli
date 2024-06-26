rank_premise = 15
rank_hypothesis = 65
class_size_premise = 47
class_size_hypothesis = 47

# the hypothesis talks about Nitin's rank in a class, which is also mentioned in the premise
if rank_hypothesis <= rank_premise:
    # check if the hypothesis value contradicts the rank of 'rank_premise'
    label = "contradiction"
elif class_size_hypothesis!= class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
