export_goods_services_premise = 1.44e12
import_goods_services_premise = 2.2e12
export_goods_services_hypothesis = 1.05e10

# the hypothesis talks about the percentage change in US exports, which is not referenced in the premise.
# the hypothesis cannot be entailed from the premise, since the percentage change in exports is unknown.
label = "neutral"

print(label)
