premise_person1 = "The two"
premise_person2 = "Barack Obama"
premise_person3 = "John McCain"
hypothesis_person1 = "Barack Obama"
hypothesis_person2 = "John McCain"

if premise_person1!= hypothesis_person1 or premise_person2!= hypothesis_person2:
    label = "contradiction"
else:
    label = "entailment"

print(label)
