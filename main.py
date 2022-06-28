acct_bal = int(input("Enter account balance: Php "))
acct_int = int(input("Enter account interest: "))
month_mature = int(input("Enter the number of months until maturity: "))

rate_fraction = acct_int/100.0
old_int = acct_bal * (rate_fraction * (month_mature/12.0))
old_bal = acct_bal + old_int

new_fraction = (acct_int * 2)/100.0
new_int = old_bal * (new_fraction * (month_mature/12.0))
new_bal = old_bal + new_int

print("\n")
print("Old Account")
print("When your CD Matures in", month_mature, "months, it will have a balance of Php", old_bal)

print("\n")
print("New Account")
print("When your CD matures in", month_mature, "months, it will have a balance of Php", new_bal)
