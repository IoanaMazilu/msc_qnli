# the hypothesis talks about the quantity of kiwi fruit, which is also mentioned in the premise
# however, the hypothesis does not mention the average rate of purchase, which is mentioned in the premise

if quantity_kiwi_fruit_hypothesis <= 5:
    # if the quantity of kiwi fruit in the hypothesis is less than or equal to 5, it is consistent with the premise
    label = "entailment"
else:
    # if the quantity of kiwi fruit in the hypothesis is greater than 5, it contradicts the premise
    label = "contradiction"

print(label)
