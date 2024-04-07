# Premise: In a group of 60 people, 35 have visited Iceland and 23 have visited Norway.
# Hypothesis: In a group of more than 20 people, 35 have visited Iceland and 23 have visited Norway.
# Golden Label: entailment

total_people_premise = 60
total_people_hypothesis = 20
visited_iceland_premise = 35
visited_iceland_hypothesis = 35
visited_norway_premise = 23
visited_norway_hypothesis = 23

# the hypothesis refers to the same group of people, the number of people who visited Iceland and Norway as mentioned in the premise
if total_people_premise <= total_people_hypothesis:
    # check if the estimate of 'total_people_hypothesis' contradicts the number of total people in the premise
    label = "contradiction"
elif visited_iceland_premise != visited_iceland_hypothesis:
    # check if the number of people who visited Iceland in the hypothesis contradicts the number of people who visited Iceland reported in the premise
    label = "contradiction"
elif visited_norway_premise != visited_norway_hypothesis:
    # check if the number of people who visited Norway in the hypothesis contradicts the number of people who visited Norway reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

