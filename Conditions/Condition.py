# 30. เขียนโค้ดเพื่อทําตามโจทย์ต่อไปนี้
# - มีตัวแปร monday และ thursday เก็บค่าข้อความจากคําสั่ง input()
# - ถ้า monday เท่ากับ “วันจันทร์” ให้แสดงข้อความว่า “สะกดวันจันทร์ถูกต้อง”
# - ถ้าเงื่อนไขข้างบนไม่ถูกต้อง ให้แสดงข้อความว่า “สะกดวันจันทร์ไม่ถูกต้อง”
# - ถ้า thursday เท่ากับ “วันพฤหัส” ให้แสดงข้อความว่า “สะกดวันพฤหัสถูกต้อง”
# - ถ้าเงื่อนไขข้างบนไม่ถูกต้อง ให้แสดงข้อความว่า “สะกดวันพฤหัสไม่ถูกต้อง”

# ตัวอย่างผลลัพธ์
# Monday ภาษาไทย : วันจัน
# Thursday ภาษาไทย : วันพฤหัส
# สะกดวันจันทร์ไม่ถูกต้อง
# สะกดวันพฤหัสถูกต้อง

# monday = input('Monday ภาษาไทย: ')
# thursday = input('Thursday ภาษาไทย: ')
# result_monday = 'สะกดวันจันทร์ถูกต้อง' if monday == 'วันจันทร์' else 'สะกดวันจันทร์ไม่ถูกต้อง'
# result_thursday = 'สะกดวันพฤหัสถูกต้อง' if monday == 'วันจันทร์' else 'สะกดวันพฤหัสไม่ถูกต้อง'
# print(f'Monday ภาษาไทย: {monday}')
# print(f'Thursday ภาษาไทย: {thursday}')
# print(f'{result_monday}')
# print(f'{result_thursday}')

# 2. คํานวณค่า x ลบ y ถ้าหาก x มีค่ามากกว่า y และ y มีค่ามากกว่า 0 โดยเราจะกรอกค่า x, y มาให้โปรแกรมใช้ต่อ

# ตัวอย่างผลลัพธ์
# Enter x : 4
# Enter y : 3
# x - y = 1

# x = int(input('Enter x: '))
# y = int(input('Enter y: '))
# print('Enter x: {x}')
# print('Enter y: {y}')
# if x  > y and y > 0:
#     print(f'x - y = {x - y}')
# else:
#     print('ป้อนข้อมูลไม่ถูกต้อง')

# 3. คํานวณค่า x หาร y ถ้าหาก y ไม่ใช่ 0 กับ 1 โดยเราจะกรอกค่า x, y มาให้โปรแกรมใช้ต่อ
# ตัวอย่างผลลัพธ์
# Enter x : 9.6
# Enter y : 2.4
# x / y = 4

x = float(input('Enter x: '))
y = float(input('Enter y: '))
# result = x/y if y!=0 and y!=1 else "Please enter a valid value"
# print(f'Enter x: {x}')
# print(f'Enter y: {y}')
# print(f'x / y = {result}')

if y!=0 and y!=1:
    print(f'x / y = {x/y}')
else:
    print('Please enter a valid value')