premise_peacekeepers = 11800
premise_african_peacekeeping_forces = 6500
premise_french_troops = 2000

hypothesis_peacekeepers = 11800

if hypothesis_peacekeepers!= premise_peacekeepers:
    label = "contradiction"
else:
    label = "entailment"

print(label)
