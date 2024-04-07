# Premise: In a group of 60 people, 35 have visited Iceland and 23 have visited Norway.
# Hypothesis: In a group of 40 people, 35 have visited Iceland and 23 have visited Norway.
# Golden Label: contradiction

total_people_premise = 60
total_people_hypothesis = 40

visited_iceland_premise = 35
visited_iceland_hypothesis = 35

visited_norway_premise = 23
visited_norway_hypothesis = 23

# the hypothesis refers to the total number of people and the number of people who have visited Iceland and Norway mentioned in the premise
if total_people_hypothesis > total_people_premise:
    # check if the total number of people in the hypothesis contradicts the total number of people in the premise
    label = "contradiction"
elif visited_iceland_hypothesis != visited_iceland_premise:
    # check if the number of people who have visited Iceland in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif visited_norway_hypothesis != visited_norway_premise:
    # check if the number of people who have visited Norway in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # the premise gives exact numbers for the total people and for those who visited Iceland and Norway
    # but the total number of people in hypothesis is less than the premise which cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

