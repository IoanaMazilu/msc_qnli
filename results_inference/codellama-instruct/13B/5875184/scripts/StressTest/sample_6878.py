amar_age = 20
akbar_age = 25
anthony_age = 31

total_ages = amar_age + akbar_age + anthony_age

if total_ages < 66:
    label = "entailment"
elif total_ages == 66:
    label = "neutral"
else:
    label = "contradiction"

print(label)
