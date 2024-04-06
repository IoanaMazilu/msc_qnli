# Premise: Recalls of the products by the Yashili and Suokang companies have been made, and of China's 175 baby milk powder production companies, 66 have already stopped production, Li said.
# Hypothesis: China's largest milk, Mengniu Dairy Group, recalls three batches of formula.
# Golden Label: neutral

recalled_companies_premise = ["Yashili", "Suokang"]
stopped_production_companies_premise = 66
total_companies_premise = 175
recalled_company_hypothesis = "Mengniu Dairy Group"

# the hypothesis mentions a company's product recall which is not mentioned in the premise
# the premise provides information about other companies' recalls and stoppage of production
# there's no contradiction or entailment between the premise and hypothesis
label = "neutral"

print(label)

