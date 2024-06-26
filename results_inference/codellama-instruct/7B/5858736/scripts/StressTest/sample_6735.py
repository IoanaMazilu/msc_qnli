rohit_days_premise = 12
rohan_days_premise = 6
rohit_days_hypothesis = 22
rohan_days_hypothesis = 6

if rohit_days_hypothesis <= rohit_days_premise:
    label = "contradiction"
elif rohan_days_hypothesis!= rohan_days_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
