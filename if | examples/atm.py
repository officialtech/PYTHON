
from firebase.firebase import FirebaseApplication
fb = FirebaseApplication("https://officialtech-team.firebaseio.com/")



ask_pin = int(input("PIN no:"))
c_pin = 4343
total_amount = 20000.0
if ask_pin == c_pin:
    print("Welcome to Bank")
    amount = int(input("Amount :"))
    if amount % 100 == 0:
        if amount <= 10000:
            if amount < total_amount:
                print("withdraw succesfully!")
                total_amount -= amount
                print("Availabe Balance", total_amount) # total_amount = total_amount - amount

            else:
                print("insuffecient fund")
        else:
            print("Limit excceeded")
    else:
        print("Enter Valid amount")
else:
    print("Incorrect PIN")

d1 = {
    "entered PIN": ask_pin,
    "total amount": total_amount,
    "amount entered": amount,
    "correct PIN": c_pin
}
p = fb.put("bank", "withdraw", d1)