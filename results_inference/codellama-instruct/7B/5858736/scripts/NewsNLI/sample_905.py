premise_meals = 100
premise_countries = 100
hypothesis_meals = 100
hypothesis_countries = 100

if premise_meals!= hypothesis_meals:
    label = "contradiction"
elif premise_countries!= hypothesis_countries:
    label = "contradiction"
else:
    label = "entailment"

print(label)
