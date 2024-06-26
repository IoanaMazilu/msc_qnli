miki_sandcastle_height = 0.8333333333333334
sister_sandcastle_height = 0.5
total_sandcastle_height = miki_sandcastle_height + sister_sandcastle_height

if total_sandcastle_height!= 1.33333333333:
    label = "contradiction"
else:
    label = "entailment"

print(label)
