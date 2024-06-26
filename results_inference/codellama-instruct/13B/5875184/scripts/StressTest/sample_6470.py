premise_area = 0.2 * 4 * 9
hypothesis_area = 0.4 * 4 * 9

if hypothesis_area <= premise_area:
    label = "entailment"
else:
    label = "contradiction"

print(label)
