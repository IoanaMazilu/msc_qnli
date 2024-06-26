premise = "In Kaya's teacher's desk there are 9 pink highlighters, 8 yellow highlighters, and 5 blue highlighters."
hypothesis = "In Kaya's teacher's desk there are more than 7 pink highlighters, 8 yellow highlighters, and 5 blue highlighters."

# extract the quantities from the premise
premise_quantities = premise.split()
premise_quantities = [int(q) for q in premise_quantities if q.isdigit()]

# extract the quantities from the hypothesis
hypothesis_quantities = hypothesis.split()
hypothesis_quantities = [int(q) for q in hypothesis_quantities if q.isdigit()]

# check if the hypothesis quantities contradict the premise quantities
if hypothesis_quantities[0] <= premise_quantities[0]:
    label = "contradiction"
elif hypothesis_quantities[1]!= premise_quantities[1]:
    label = "contradiction"
elif hypothesis_quantities[2]!= premise_quantities[2]:
    label = "contradiction"
else:
    label = "neutral"

print(label)
