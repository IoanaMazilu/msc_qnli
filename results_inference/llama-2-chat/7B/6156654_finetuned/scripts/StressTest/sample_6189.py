# The hypothesis refers to the number of days Lexi needs to save to afford a vacation
# and the premise gives the number of days and the salary
days_to_save_hypothesis = 80
days_to_save_premise = 30
salary_premise = 125

# The hypothesis and premise mention the same event, but with different numbers
# We can't infer entailment or contradiction, as the hypothesis is a specific case
# of the premise, so we mark it as neutral
label = "neutral"

print(label)
