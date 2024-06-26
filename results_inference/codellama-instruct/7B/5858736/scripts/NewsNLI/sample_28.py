premise_gross_revenue = 29300000
hypothesis_gross_revenue = 29300000

if hypothesis_gross_revenue!= premise_gross_revenue:
    label = "contradiction"
else:
    label = "entailment"

print(label)
