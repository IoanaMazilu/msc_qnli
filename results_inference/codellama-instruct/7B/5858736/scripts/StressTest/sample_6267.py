premise_death_bombardment = 10
premise_fear_remainder = 20
hypothesis_death_bombardment = 30
hypothesis_fear_remainder = 20

# the hypothesis refers to the number of people who died by bombardment and the remainder who left the village
if hypothesis_death_bombardment <= premise_death_bombardment:
    # check if the estimate of 'hypothesis_death_bombardment' contradicts the number of people who died by bombardment in the premise
    label = "contradiction"
elif hypothesis_fear_remainder!= premise_fear_remainder:
    # check if the number of people who left the village in the hypothesis contradicts the number of people who left the village reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
