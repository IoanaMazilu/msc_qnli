premise = "Kiran is younger than Bineesh by more than 6 years and their ages are in the respective ratio of 7:9."
hypothesis = "Kiran is younger than Bineesh by 7 years and their ages are in the respective ratio of 7:9."

# extract the numerical entities from the premise
premise_ages = premise.split("by")[1].split("and")[0].strip()
premise_ratio = premise.split("and")[1].split("of")[0].strip()

# extract the numerical entities from the hypothesis
hypothesis_ages = hypothesis.split("by")[1].strip()
hypothesis_ratio = hypothesis.split("of")[1].strip()

# convert the numerical entities to integers
premise_ages = int(premise_ages)
premise_ratio = int(premise_ratio)
hypothesis_ages = int(hypothesis_ages)
hypothesis_ratio = int(hypothesis_ratio)

# check if the hypothesis values contradict the premise values
if hypothesis_ages < premise_ages:
    label = "contradiction"
elif hypothesis_ratio!= premise_ratio:
    label = "contradiction"
else:
    label = "entailment"

print(label)
