people_fled_premise = 2
people_fled_hypothesis = 5

# the hypothesis mentions the number of people fleeing the cafe, which is also mentioned in the premise
if people_fled_hypothesis > people_fled_premise:
    # check if the number of people fleeing in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the number of people fleeing in the hypothesis does not contradict the number from the premise, we have either entailment or neutrality
    label = "entailment" if people_fled_hypothesis == people_fled_premise else "neutral"

print(label)
