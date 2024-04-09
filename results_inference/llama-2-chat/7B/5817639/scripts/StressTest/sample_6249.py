boys_premise = 6
girls_premise = 4
boys_hypothesis = 5
girls_hypothesis = 4

# the hypothesis talks about the gender distribution in the formation of a committee, referenced also in the premise
if boys_hypothesis <= boys_premise:
    # check if the hypothesis value contradicts the estimate of 'boys_premise'
    label = "contradiction"
elif girls_hypothesis!= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
