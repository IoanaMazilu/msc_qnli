apples_premise = 10
oranges_premise = 10
total_fruit_premise = apples_premise + oranges_premise
average_price_premise = 56

# the hypothesis refers to the same quantities as the premise
apples_hypothesis = 10
oranges_hypothesis = 10
total_fruit_hypothesis = apples_hypothesis + oranges_hypothesis
average_price_hypothesis = 56

# the hypothesis does not contradict the premise
contradiction = False

# the premise does not entail the hypothesis
entailment = False

# if the hypothesis values contradict the premise values, we can infer entailment
if apples_hypothesis!= apples_premise or oranges_hypothesis!= oranges_premise or total_fruit_hypothesis!= total_fruit_premise or average_price_hypothesis!= average_price_premise:
    contradiction = True
elif apples_hypothesis == apples_premise and oranges_hypothesis == oranges_premise and total_fruit_hypothesis == total_fruit_premise and average_price_hypothesis == average_price_premise:
    entailment = True

print(f"contradiction: {contradiction}")
print(f"entailment: {entailment}")
