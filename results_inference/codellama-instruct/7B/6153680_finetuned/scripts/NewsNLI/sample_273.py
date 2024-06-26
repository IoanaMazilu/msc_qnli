# The hypothesis and premise both mention the cost of renovation for the bishop's residence in Limburg, Germany
# The hypothesis states the cost of renovation, while the premise states the bishop is under investigation for his spending

label = "neutral"

# The hypothesis and premise both mention the cost of renovation for the bishop's residence in Limburg, Germany
# The hypothesis states the cost of renovation, while the premise states the bishop is under investigation for his spending

if hypothesis!= premise:
    # If the hypothesis and premise are different, then the hypothesis contradicts the premise
    label = "contradiction"

print(label)
