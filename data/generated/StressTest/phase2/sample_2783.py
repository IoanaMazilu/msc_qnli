# Premise: In a group of 50 people, 25 have visited Iceland and 23 have visited Norway.
# Hypothesis: In a group of 60 people, 25 have visited Iceland and 23 have visited Norway.
# Golden Label: contradiction

group_size_premise = 50
group_size_hypothesis = 60
visited_iceland_premise = 25
visited_iceland_hypothesis = 25
visited_norway_premise = 23
visited_norway_hypothesis = 23

# the hypothesis talks about the size of a group and the number of people who have visited Iceland and Norway, all mentioned in the premise
if group_size_hypothesis != group_size_premise:
    # check if the group size in the hypothesis contradicts the group size reported in the premise
    label = "contradiction"
elif visited_iceland_hypothesis != visited_iceland_premise:
    # check if the number of people who have visited Iceland in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif visited_norway_hypothesis != visited_norway_premise:
    # check if the number of people who have visited Norway in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if all the values in the hypothesis match the values given in the premise, we can infer entailment
    label = "entailment"

print(label)

