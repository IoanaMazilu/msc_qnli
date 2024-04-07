# Premise: In a group of less than 70 people, 25 have visited Iceland and 23 have visited Norway.
# Hypothesis: In a group of 50 people, 25 have visited Iceland and 23 have visited Norway.
# Golden Label: neutral

people_group_premise = 70
people_group_hypothesis = 50
visited_iceland_premise = 25
visited_iceland_hypothesis = 25
visited_norway_premise = 23
visited_norway_hypothesis = 23

# the hypothesis discusses the same topics as the premise, regarding the number of people and their travels
if people_group_hypothesis >= people_group_premise:
    # check if the number of people in the hypothesis contradicts the 'less than' condition in the premise
    label = "contradiction"
elif visited_iceland_hypothesis != visited_iceland_premise or visited_norway_hypothesis != visited_norway_premise:
    # check if the number of people who visited Iceland or Norway in the hypothesis contradicts the numbers in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

