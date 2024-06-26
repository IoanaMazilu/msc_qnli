veena_rank_premise = 73
veena_rank_hypothesis = 73
class_size_premise = 182
class_size_hypothesis = 182

# the hypothesis talks about Veena's rank in a class, referenced also in the premise
if veena_rank_hypothesis != veena_rank_premise:
    # check if the hypothesis value contradicts the exact rank of Veena in the premise
    label = "contradiction"
elif class_size_hypothesis != class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, but the premise does not entail that Veena ranks more than 73rd
    label = "neutral"

print(label)
