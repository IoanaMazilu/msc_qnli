# Premise: Still, violence continued:Insurgents killed five U.S. soldiers, set off a suicide car bomb that killed four Iraqi policemen in Baghdad and targeted more polling sites across the country.
# Hypothesis: Five US soldiers were killed, and at least 10 Iraqis died in Baghdad.
# Golden Label: neutral

us_soldiers_killed_premise = 5
us_soldiers_killed_hypothesis = 5
iraqis_killed_premise = 4
iraqis_killed_hypothesis = 10

# the hypothesis talks about the number of US soldiers and Iraqis killed, which is also mentioned in the premise
if us_soldiers_killed_hypothesis != us_soldiers_killed_premise:
    # check if the number of US soldiers killed in the hypothesis contradicts the number from the premise
    label = "contradiction"
elif iraqis_killed_hypothesis < iraqis_killed_premise:
    # check if the number of Iraqis killed in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

