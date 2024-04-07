# Premise: In a group of 100 people, 55 have visited Iceland and 43 have visited Norway.
# Hypothesis: In a group of less than 600 people, 55 have visited Iceland and 43 have visited Norway.
# Golden Label: entailment

total_people_premise = 100
total_people_hypothesis = 600
iceland_visitors_premise = 55
iceland_visitors_hypothesis = 55
norway_visitors_premise = 43
norway_visitors_hypothesis = 43

# the hypothesis talks about the number of people in a group and the number of Iceland and Norway visitors, all mentioned in the premise
if total_people_hypothesis < total_people_premise:
    # check if the total people estimate in the hypothesis contradicts the total people count in the premise
    label = "contradiction"
elif iceland_visitors_hypothesis != iceland_visitors_premise:
    # check if the number of Iceland visitors in the hypothesis contradicts the number of Iceland visitors reported in the premise
    label = "contradiction"
elif norway_visitors_hypothesis != norway_visitors_premise:
    # check if the number of Norway visitors in the hypothesis contradicts the number of Norway visitors reported in the premise
    label = "contradiction"
else:
    # the premise values do not contradict with the hypothesis estimates, but because the group size in the hypothesis is a range and not an exact value, we can infer neutrality
    label = "neutral"

print(label)

