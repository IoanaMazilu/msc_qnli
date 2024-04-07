# Premise: In a group of 90 people, 55 have visited Iceland and 33 have visited Norway.
# Hypothesis: In a group of more than 90 people, 55 have visited Iceland and 33 have visited Norway.
# Golden Label: contradiction

group_size_premise = 90
group_size_hypothesis = 90
iceland_visitors_premise = 55
iceland_visitors_hypothesis = 55
norway_visitors_premise = 33
norway_visitors_hypothesis = 33

# the hypothesis refers to the group size and the number of visitors to Iceland and Norway mentioned in the premise
if group_size_hypothesis > group_size_premise:
    # check if the hypothesis value contradicts the exact number of people in the group reported in the premise
    label = "contradiction"
elif iceland_visitors_hypothesis != iceland_visitors_premise or norway_visitors_hypothesis != norway_visitors_premise:
    # check if the number of visitors to Iceland or Norway in the hypothesis contradicts the numbers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

