# Premise: In a group of 50 people, 25 have visited Iceland and 23 have visited Norway.
# Hypothesis: In a group of less than 70 people, 25 have visited Iceland and 23 have visited Norway.
# Golden Label: entailment

total_people_premise = 50
total_people_hypothesis = 70
iceland_visitors_premise = 25
iceland_visitors_hypothesis = 25
norway_visitors_premise = 23
norway_visitors_hypothesis = 23

# the hypothesis refers to the number of people, and the number of visitors to Iceland and Norway mentioned in the premise
if total_people_premise >= total_people_hypothesis:
    # check if the estimate of 'total_people_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
elif iceland_visitors_premise != iceland_visitors_hypothesis:
    # check if the number of visitors to Iceland in the hypothesis contradicts the number of visitors to Iceland reported in the premise
    label = "contradiction"
elif norway_visitors_premise != norway_visitors_hypothesis:
    # check if the number of visitors to Norway in the hypothesis contradicts the number of visitors to Norway reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

