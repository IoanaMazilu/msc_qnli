# Premise: About 450 people have been injured in clashes, according to the Pakistan Institute of Medical Sciences and Polytechnic Hospital.
# Hypothesis: About 450 people were injured in clashes, health officials say.
# Golden Label: entailment

injured_people_premise = 450
injured_people_hypothesis = 450

# the hypothesis mentions the number of injured people, which is also mentioned in the premise
if injured_people_hypothesis != injured_people_premise:
    # check if the number of injured people from the hypothesis contradicts the number given in the premise
    label = "contradiction"
else:
    # if the number of injured people in the hypothesis does not contradict the number from the premise, we can infer entailment
    label = "entailment"

print(label)

