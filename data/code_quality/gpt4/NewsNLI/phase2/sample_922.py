recalled_companies_premise = ["Yashili", "Suokang"]
stopped_production_companies_premise = 66
total_companies_premise = 175
recalled_company_hypothesis = "Mengniu Dairy Group"

# the hypothesis mentions a company's product recall which is not mentioned in the premise
# the premise provides information about other companies' recalls and stoppage of production
# there's no contradiction or entailment between the premise and hypothesis
label = "neutral"

print(label)
