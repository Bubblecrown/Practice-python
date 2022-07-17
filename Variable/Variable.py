#########################################

# No.2
# x = int(input('Enter your first number:'))
# y = int(input('Enter your secont number:'))
# z = (2*x) + (2*y)
# print(z)

# No. 3 
# x = int(input('Enter your first number:'))
# y = 2*(x + 1)
# print(y)

# No. 7
# x = int(input('Enter your number: '))
# y = x**2 + 2*x + 1
# print(y)

# No. 8
# x = int(input('Enter your first number: '))
# y = int(input('Enter your second number: '))
# print(x**2 + 2*x*y + y**2)

# No. 10
# x = int(input('Enter your first number: '))
# y = int(input('Enter your second number: '))
# print(6 + 2 * y - 5 - 3 * x)

#########################################

# 1 roti
# roti = int(input('Amount of roti: '))
# price_roti = 30
# total = roti * price_roti
# text='บาท'
# print(f"{total} {text}")

# 2 taro and pork bread
# taro = int(input('เผือกทอดจำนวน: '))
# pork_bread = int(input('ขนมปังหน้าหมูจำนวน: '))
# taro_price = 30
# pork_bread_price = 40
# total = (taro_price * taro) + (pork_bread_price * pork_bread)
# print(f"{total} บาท")

# 4 income-expenses
# incomeFirst = int(input('รายรับเ้ดือนที่ 1: '))
# expensesFirst = int(input('รายจ่ายเ้ดือนที่ 1: '))
# incomeSecond = int(input('รายรับเ้ดือนที่ 2: '))
# expensesSecond = int(input('รายจ่ายเ้ดือนที่ 2: '))
# profitFirst = incomeFirst - expensesFirst
# profitSecond = incomeSecond - expensesSecond
# print(f'กําไรรวม 2 เดือน = {profitFirst + profitSecond} บาท')

# 5 Mile to kelometer
# def mileToKmeter(mile):
#     return mile*1.6

# distanceMile = int(input('ระยะทางไมล์: '))
# print(f'{mileToKmeter(distanceMile)} กิโลเมตร')

# 6 BMI
# def bmi(w, h):
#     return w/(h/100)**2
# weight = int(input('กรุณาระบุน้ำหนักของคุณ: '))
# height = int(input('กรุณาระบุส่วนสูงของคุณ: '))
# print(f'น้ําหนัก {weight} กิโลกรัม, ส่วนสูง {height/100} เมตร')
# print(f'BMI = {round(bmi(weight, height), 2)}') # ทศนิยม 2 ตำแหน่ง round()

# 7 คํานวณเปอร์เซ็นต์ของนักเรียนที่สอบผ่าน และสอบตกจากนักเรียนทั้งหมดในห้อง
# def gradePercantage(total, totalPass):
#     return 100*totalPass/total

# student = int(input('จำนวนนักเรียนทั้งหมด: '))
# passStudent = int(input('จำนวนนักเรียนที่สอบผ่าน: '))
# print(f'เปอร์เซ็นต์สอบผ่าน = {round(gradePercantage(student, passStudent))}')
# print(f'เปอร์เซ็นต์สอบตก = {round(100 - gradePercantage(student, passStudent))}')

# 10 คํานวณหาค่าเฉลี่ยจากตัวเลขทั้งหมด 4 ตัวเลข
listInput = [int(item) for item in input('Enter numbers: ').split()]
total = 0
for i in listInput:
    total = i + total

print(f'ตัวเลขได้แก่ {listInput}')
print(f'ค่าเฉลี่ย = {total/len(listInput)}')



