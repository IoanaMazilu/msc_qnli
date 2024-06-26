ranking_premise = 15
ranking_hypothesis = 75
class_size_premise = 47
class_size_hypothesis = 47

# the hypothesis refers to the ranking of Nitin in a class, which is also mentioned in the premise
if ranking_hypothesis >= ranking_premise:
    # check if the estimate of 'ranking_hypothesis' contradicts the ranking in the premise
    label = "contradiction"
elif class_size_hypothesis!= class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
