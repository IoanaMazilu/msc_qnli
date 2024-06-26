people_invited_premise = 18.0
people_showed_up_premise = 12.0
tables_held_premise = 3.0
tables_needed_hypothesis = 10.0

# first, extract all quantities as valid numbers
people_invited = int(people_invited_premise)
people_showed_up = int(people_showed_up_premise)
tables_held = int(tables_held_premise)
tables_needed = int(tables_needed_hypothesis)

# compare the quantities
if tables_needed > tables_held:
    # the hypothesis entails the premise
    label = "entailment"
elif tables_needed < tables_held:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis and premise are neutral
    label = "neutral"

print(label)
