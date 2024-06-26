ranking_premise = 65
ranking_hypothesis = 25
class_size_premise = 182
class_size_hypothesis = 182

# the hypothesis refers to Veena's ranking and the class size, both mentioned in the premise
if ranking_hypothesis!= ranking_premise:
    # check if the ranking in the hypothesis contradicts the ranking reported in the premise
    label = "contradiction"
elif class_size_hypothesis!= class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
