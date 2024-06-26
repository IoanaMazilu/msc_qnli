group_size_premise = 20
group_size_hypothesis = 60
iceland_visits_premise = 35
iceland_visits_hypothesis = 35
norway_visits_premise = 23
norway_visits_hypothesis = 23

# the hypothesis refers to the number of people in a group and the number of visits to Iceland and Norway
if group_size_hypothesis <= group_size_premise:
    # check if the hypothesis value contradicts the estimate of more than 'group_size_premise'
    label = "contradiction"
elif iceland_visits_hypothesis!= iceland_visits_premise or norway_visits_hypothesis!= norway_visits_premise:
    # check if the number of visits to Iceland and Norway in the hypothesis contradicts the number of visits reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
