is_entailment = compare_premise_hypothesis(premise, hypothesis)

if is_entailment == "entailment":
    print("Entailment")
elif is_entailment == "contradiction":
    print("Contradiction")
else:
    print("Neutral")
