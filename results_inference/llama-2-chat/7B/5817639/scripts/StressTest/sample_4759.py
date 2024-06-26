# Premise
premise_shirts = int(input())
premise_jeans = int(input())
premise_sneakers = int(input())

# Hypothesis
hypothesis_shirts = int(input())
hypothesis_jeans = int(input())
hypothesis_sneakers = int(input())

# Comparison
if hypothesis_shirts <= premise_shirts:
    label = "contradiction"
elif hypothesis_jeans!= premise_jeans or hypothesis_sneakers!= premise_sneakers:
    label = "contradiction"
else:
    label = "entailment"

print(label)
