candy_initially = 26.0
candy_eaten = 17.0
candy_left = candy_initially - candy_eaten

print(f"Premise: {candy_initially} pieces of candy initially")
print(f"Premise: {candy_eaten} pieces of candy eaten")
print(f"Hypothesis: {candy_left} pieces of candy left")

# the hypothesis is entailed by the premise
print(f"Entailment: {candy_left} pieces of candy left")
