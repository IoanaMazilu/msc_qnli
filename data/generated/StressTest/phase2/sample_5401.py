# Premise: In a group of more than 30 people, 45 have visited Iceland and 33 have visited Norway.
# Hypothesis: In a group of 80 people, 45 have visited Iceland and 33 have visited Norway.
# Golden Label: neutral

people_premise = 30
people_hypothesis = 80

visited_iceland_premise = 45
visited_iceland_hypothesis = 45

visited_norway_premise = 33
visited_norway_hypothesis = 33

# the hypothesis talks about the number of people in a group, and the number of people who visited Iceland and Norway, all referenced also in the premise
if visited_iceland_hypothesis != visited_iceland_premise or visited_norway_hypothesis != visited_norway_premise:
    # check if the number of people who visited Iceland and Norway in the hypothesis contradicts the number of people who visited Iceland and Norway in the premise
    label = "contradiction"
elif people_hypothesis <= people_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

