total_records_premise = 5000000
factory_records_premise = 5000000
home_records_premise = 100000
total_records_hypothesis = 5000000

# the hypothesis mentions the total number of records and suggests they are stored in two warehouses and the home
# the premise specifies the total number of records too and indicates that most of them are in a factory, with the rest in the home
# but the premise does not mention a second warehouse

if total_records_hypothesis != total_records_premise:
    # check if the total number of records in the hypothesis contradicts the total number in the premise
    label = "contradiction"
elif factory_records_premise + home_records_premise != total_records_premise:
    # check if the sum of records in the factory and home from the premise contradicts the total number in the premise
    label = "contradiction"
else:
    # total number of records is the same, but the storage locations cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
