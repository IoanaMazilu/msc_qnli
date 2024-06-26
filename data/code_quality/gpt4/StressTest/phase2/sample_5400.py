total_people_premise = 80
total_people_hypothesis = 30
iceland_visitors_premise = 45
iceland_visitors_hypothesis = 45
norway_visitors_premise = 33
norway_visitors_hypothesis = 33

# the hypothesis refers to the number of people who have visited Iceland and Norway in a certain group, as mentioned in the premise
if total_people_premise <= total_people_hypothesis:
    # check if the 'total_people_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
elif iceland_visitors_premise != iceland_visitors_hypothesis or norway_visitors_premise != norway_visitors_hypothesis:
    # check if the number of visitors in the hypothesis contradicts the number of visitors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
