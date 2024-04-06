# Premise: The death toll of a fire that roared through a packed Buenos Aires nightclub climbed on Friday to at least 175, with more than 700 injured as young revellers stampeded to reach locked exit doors.
# Hypothesis: At least 174 had been killed and more than 410 people injured.
# Golden Label: entailment

deaths_premise = 175
injured_premise = 700
deaths_hypothesis = 174
injured_hypothesis = 410

# the hypothesis talks about the number of deaths and injured people, which are also mentioned in the premise
if deaths_hypothesis > deaths_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths in the premise
    label = "contradiction"
elif injured_hypothesis > injured_premise:
    # check if the number of injured people in the hypothesis contradicts the number of injured people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

