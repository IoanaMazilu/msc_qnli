premise_people_detained = 939
hypothesis_people_arrested = 939

if premise_people_detained!= hypothesis_people_arrested:
    label = "contradiction"
else:
    label = "entailment"

print(label)
