# The hypothesis refers to the price of the stocks and the number of shares sold
# The premise gives the exact prices and number of shares sold

# The hypothesis states that the price of MicroTron stock is less than 76$/share
# The premise gives the price of MicroTron stock as 36$/share
if 36 >= 76:
    # check if the premise value contradicts the hypothesis value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
