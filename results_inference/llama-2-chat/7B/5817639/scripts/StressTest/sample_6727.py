# Premise:
total_apples_premise = 0
total_oranges_premise = 0
average_price_premise = 0
for word in premise.split():
    if "apples" in word:
        total_apples_premise += int(word.split(":")[1])
    elif "oranges" in word:
        total_oranges_premise += int(word.split(":")[1])
    else:
        average_price_premise += float(word.split(":")[1])

# Hypothesis:
total_apples_hypothesis = 10
total_oranges_hypothesis = 10
average_price_hypothesis = 56

# Comparison:
if total_apples_hypothesis <= total_apples_premise:
    label = "contradiction"
elif average_price_hypothesis!= average_price_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
