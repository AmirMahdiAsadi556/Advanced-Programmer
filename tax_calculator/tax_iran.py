salary_month = float(input("Enter your monthly salary (toman): "))
#تبدیل ماه به سال
salary_year = salary_month * 12

baze1 = 67_200_000    # tax: 0%
baze2 = 180_000_000   # tax: 10%
baze3 = 360_000_000   # tax: 15%
baze4 = 1_000_000_000 # tax: 20%

#محاسبات مالیات 
if salary_year <= baze1:
    tax = 0
elif salary_year <= baze2:
    tax = (salary_year - baze1) * 0.10
elif salary_year <= baze3:
    tax = (baze2 - baze1) * 0.10 \
          + (salary_year - baze2) * 0.15
elif salary_year <= baze4:
    tax = (baze2 - baze1) * 0.10 \
          + (baze3 - baze2) * 0.15 \
          + (salary_year - baze3) * 0.20
else:
    tax = (baze2 - baze1) * 0.10 \
          + (baze3 - baze2) * 0.15 \
          + (baze4 - baze3) * 0.20 \
          + (salary_year - baze4) * 0.30
    
print("Annual salary:" , int(salary_year), "toman")
print("Annual tax:"    , int(tax), "toman")
print("Monthly tax:" , int(tax / 12), "toman")