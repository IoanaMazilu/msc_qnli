# Premise: Two car bombs explode near a police station outside of Baghdad's Green Zone, killing seven police officers and wounding about 60 others.
# Hypothesis: 60 people are killed when a car bomb explodes near a police station in Baghdad.
# Golden Label: neutral

killed_premise = 7
wounded_premise = 60
car_bombs_premise = 2

killed_hypothesis = 60
car_bombs_hypothesis = 1

# the hypothesis talks about the number of people killed and the number of car bombs exploded, which are both mentioned in the premise
if killed_hypothesis != killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number of people killed from the premise
    label = "contradiction"
elif car_bombs_hypothesis != car_bombs_premise:
    # check if the number of car bombs in the hypothesis contradicts the number of car bombs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

