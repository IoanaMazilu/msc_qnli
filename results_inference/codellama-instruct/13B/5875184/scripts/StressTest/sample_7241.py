premise = "Ayisha's age is 1/6 th of her father's age."
hypothesis = "Ayisha's age is less than 1/6 th of her father's age."

# extract the numerical entities from the premise and hypothesis
premise_age = 1/6
hypothesis_age = 1/6

# compare the numerical entities
if premise_age > hypothesis_age:
    label = "entailment"
elif premise_age < hypothesis_age:
    label = "contradiction"
else:
    label = "neutral"

print(label)
