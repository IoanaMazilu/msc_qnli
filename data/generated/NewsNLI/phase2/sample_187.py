# Premise: Malaysia has 15777-200 s in its fleet, it's an extremely experienced operator of this type of aircraft.
# Hypothesis: Malaysia Airlines operates fleet of 15 Boeing 777-200 aircraft.
# Golden Label: entailment

fleet_premise = 15
fleet_hypothesis = 15

# the hypothesis states the number of Boeing 777-200 aircraft in Malaysia's fleet, which is also mentioned in the premise
if fleet_hypothesis != fleet_premise:
    # check if the number of aircraft in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of aircraft in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

