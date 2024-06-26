iceland_premise = 35
iceland_hypothesis = 35
norway_premise = 23
norway_hypothesis = 23

# the hypothesis refers to the number of people who have visited Iceland and Norway
if iceland_hypothesis <= iceland_premise and norway_hypothesis <= norway_premise:
    # check if the hypothesis values contradict the number of people who have visited Iceland and Norway reported in the premise
    label = "contradiction"
elif iceland_hypothesis!= iceland_premise or norway_hypothesis!= norway_premise:
    # check if the number of people who have visited Iceland and Norway in the hypothesis contradicts the number of people who have visited Iceland and Norway reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)