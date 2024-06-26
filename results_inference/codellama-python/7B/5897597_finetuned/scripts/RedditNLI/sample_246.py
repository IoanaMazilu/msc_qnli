weeks_premise = 2
weeks_hypothesis = 2

# гіпотеза та припустка містять число тижнів між суперечливим дослідженням і відповіді ECB
if weeks_hypothesis!= weeks_premise:
    # перевірка, чи не збігається число тижнів в гіпотезі з числом тижнів в припустці
    label = "contradiction"
else:
    # якщо числа тижнів в гіпотезі і припустці не суперечать, ми можемо вивести відношення
    label = "entailment"

print(label)
