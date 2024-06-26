# Define variables for the numerical entities in the premise and hypothesis
kiwi_fruit_bought_premise = 8
kiwi_fruit_bought_hypothesis = 5
kiwi_fruit_rate_premise = 360
kiwi_fruit_rate_hypothesis = 360

# Check if the hypothesis value contradicts the premise
if kiwi_fruit_bought_hypothesis <= kiwi_fruit_bought_premise:
    label = "contradiction"
elif kiwi_fruit_rate_hypothesis!= kiwi_fruit_rate_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
