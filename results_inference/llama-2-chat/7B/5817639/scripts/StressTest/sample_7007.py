gerbils_premise = 96
hamsters_premise = 96
gerbils_hypothesis = 66
hamsters_hypothesis = 66

# the hypothesis talks about the total number of pets consisting of gerbils and hamsters, referenced also in the premise
if gerbils_hypothesis <= gerbils_premise:
    # check if the hypothesis value contradicts the estimate of 'gerbils_premise'
    label = "contradiction"
elif hamsters_hypothesis!= hamsters_premise:
    # check if the number of hamsters in the hypothesis contradicts the number of hamsters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
