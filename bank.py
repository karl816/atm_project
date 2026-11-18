
print("-----------BANK------------")
bank_account = 0
wallet = 0

while True:
    bk = input("Would you like to deposit or withdraw ? press (D/W) or x to quit: ").lower()

    if bk == "d":
        deposit = float(input("How much do you want to deposit ?: "))
        if isinstance(deposit, (int, float)):
            bank_account += deposit
            print("Your balance has been successfully deposited !")
            print(f"Bank account: ${bank_account:.2f}")

    elif bk == "w":
        withdraw = float(input("How much do you want to withdraw ?: "))
        bank_account -= withdraw
        wallet += withdraw
        if bank_account < 0:
            print("Sorry, you don't have enough money in your bank account to withdraw")
            break
        else:
            print("Withdrawal successfully executed !")
            print(f"Bank account: ${bank_account}")
            print(f"Wallet: ${wallet}")

    else:
        if bk == "x":
            print("Bye, see you !")
            break
print("-----------------------------")