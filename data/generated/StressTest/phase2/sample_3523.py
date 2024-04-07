# Premise: In a group of less than 600 people, 55 have visited Iceland and 43 have visited Norway.
# Hypothesis: In a group of 100 people, 55 have visited Iceland and 43 have visited Norway.
# Golden Label: neutral

group_size_premise = 600
group_size_hypothesis = 100
visited_iceland_premise = 55
visited_iceland_hypothesis = 55
visited_norway_premise = 43
visited_norway_hypothesis = 43

# the hypothesis refers to the group size and the number of people who visited Iceland and Norway mentioned in the premise
if group_size_hypothesis >= group_size_premise:
    # check if the 'group_size_hypothesis' contradicts the estimate of less than 'group_size_premise'
    label = "contradiction"
elif visited_iceland_hypothesis != visited_iceland_premise or visited_norway_hypothesis != visited_norway_premise:
    # check if the number of people who visited Iceland and Norway in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

