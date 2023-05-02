from datetime import datetime

#------FUNCTION FOR GETTING THE SUBTOTAL-------------------------
def calculate_subtotal(sub_total, discountrate):
    discount = round(sub_total * discountrate, 2)
    print(f"Discount amount: {discount:.2f}")
    sub_total -= discount
    return sub_total

#------FUNCTION FOR CALCULATING THE SALES TAX---------------------
def get_sales_tax(subtotal, salestax):
    sales_tax = round(subtotal * salestax, 2)
    print(f'Sales tax amount: {sales_tax:.2f}')
    return sales_tax

#------DISCOUNT RATE 10% AND SALES TAX 6%-------------------------
discountRate = 0.10
salesTax = 0.06

#------ASK THE USER FOR THE SUBTOTAL------------------------------
subTotal = float(input('Please enter the subtotal: '))

#------THIS FUNCTION WILL GET YOUR CURRENT DAY OF THE WEEK -------
current_date_time = datetime.now()

#------GET THE DAY FROM current_date_time-------------------------
weekday = current_date_time.weekday()

#--------IF SUBTOTAL IS LESS THAN 50 DOLLARS-----------------------
if subTotal < 50:
    difference = 50 - subTotal

#-------CALLING THE FUNCTION---------------------------------------
new_sales_tax = get_sales_tax(subtotal=subTotal, salestax=salesTax)

if subTotal >= 50 and (weekday == 1 or weekday ==2):  
    new_subtotal = calculate_subtotal(sub_total=subTotal, discountrate=discountRate)
    total = new_subtotal + new_sales_tax

#-------CALCULATING THE TOTAL---------------------------------------
else:
    total = subTotal + new_sales_tax
    new_difference = difference - new_sales_tax
#--------OUTPUT------------------------------------------------------
print(f'Total: {total:.2f}')
print()
print(f"You need to spend {new_difference:.2f} to earn 10 percent off.")
