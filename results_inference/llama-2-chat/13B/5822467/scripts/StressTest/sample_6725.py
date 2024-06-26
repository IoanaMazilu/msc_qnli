anwar_premise = 3600
anwar_hypothesis = float(input("Enter the amount from Anwar: "))
percentage_premise = 6

# convert the hypothesis to the same percentage as the premise
hypothesis_percentage = percentage_premise * anwar_hypothesis / 100

# check if the hypothesis value contradicts the premise value
if anwar_hypothesis > anwar_premise:
    label = "contradiction"
elif hypothesis_percentage > percentage_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
