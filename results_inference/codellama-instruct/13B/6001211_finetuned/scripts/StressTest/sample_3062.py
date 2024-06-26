boys_premise = 6
boys_hypothesis = 6
girls_premise = 4
girls_hypothesis = 4
committee_premise = 4
committee_hypothesis = 4

# the hypothesis refers to the number of boys, girls, and committee size mentioned in the premise
if boys_hypothesis >= boys_premise:
    # check if the estimate of 'boys_hypothesis' contradicts the number of boys in the premise
    label = "contradiction"
elif girls_hypothesis!= girls_premise or committee_hypothesis!= committee_premise:
    # check if the number of girls or committee size in the hypothesis contradicts the number of girls or committee size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
