# Premise: There were no immediate reports of injuries, and authorities said they found no signs of fires at any other church in Greenville, which is about 75 miles east of Raleigh.
# Hypothesis: Greenville is located about 75 miles east of Raleigh.
# Golden Label: entailment

distance_premise = 75
distance_hypothesis = 75

# the hypothesis talks about the distance from Greenville to Raleigh, which is also mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the distance in the premise, we can infer entailment
    label = "entailment"

print(label)

