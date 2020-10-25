try:
    annual_salary = int(input("What is your annual salary: £"))
except:
    print("Please input a numeric amount (w/o currency symbol)")
    quit()
# PA up to £12,500, 20% to £50k, 40% to £150k, Over 45%
# NIC -£792 0%, £792-£4,167 12%, > £4,167 2%
# Annual NIC: £9,504 0%, - £50,004 12%, > £50,004 2%
basic_txr = 0.2
higher_txr = 0.4
add_txr = 0.45
basic_nic_rt = 0.12
higher_nic_rt = 0.02
nic_floor = 9504
nic_base = 50004
p_allow = 12500
basic_pay = 37500
higher_pay = 100000

if annual_salary <= 12500:
    if annual_salary >= 9504:
        basic_nic = int((annual_salary - nic_floor) * basic_nic_rt)
        take_home_pay = int(annual_salary - basic_nic)
    take_home_pay = int(annual_salary)
    print("Personal Allowance: £" + str(annual_salary))
    if annual_salary >= nic_floor:
        print(("NIC @ 12%: £") + str(basic_nic))
    print("Your net salary is: £" + str(take_home_pay))
elif annual_salary <= 50000:
    basic_pay = int(annual_salary - 12500)
    b_tax_tot = int(basic_pay * basic_txr)
    basic_nic = int((annual_salary - nic_floor) * basic_nic_rt)
    take_home_pay = int(annual_salary - (b_tax_tot + basic_nic))
    print("Personal Allowance: £" + str(p_allow))
    print("Basic-rate pay: £" + str(basic_pay))
    print("Basic-rate tax @ 20%: £" + str(b_tax_tot))
    print(("NIC @ 12%: £") + str(basic_nic))
    print("Your net salary is: £" + str(take_home_pay))
elif annual_salary <= 150000:
    higher_pay = int(annual_salary - 50000)
    b_tax_tot = int(basic_pay * basic_txr)
    h_tax_tot = int(higher_pay * higher_txr)

    if annual_salary <= nic_base:
        basic_nic = int((annual_salary - nic_floor) * basic_nic_rt)
        take_home_pay = int(annual_salary - (b_tax_tot + h_tax_tot + basic_nic))
        print("Personal Allowance: £" + str(p_allow))
        print("Basic-rate pay: £" + str(basic_pay))
        print("Higher-rate pay: £" + str(higher_pay))
        print("Basic-rate tax @ 20%: £" + str(b_tax_tot))
        print("Higher-rate tax @ 40%: £" + str(h_tax_tot))
        print(("NIC @ 12%: £") + str(basic_nic))
        print("Your net salary is: £" + str(take_home_pay))
    else:
        basic_nic = int((nic_base - nic_floor) * basic_nic_rt)
        higher_nic = int((annual_salary - nic_base) * higher_nic_rt)
        take_home_pay = int(annual_salary - (b_tax_tot + h_tax_tot + basic_nic + higher_nic))
        print("Personal Allowance: £" + str(p_allow))
        print("Basic-rate pay: £" + str(basic_pay))
        print("Higher-rate pay: £" + str(higher_pay))
        print("Basic-rate tax @ 20%: £" + str(b_tax_tot))
        print("Higher-rate tax @ 40%: £" + str(h_tax_tot))
        print(("NIC @ 12%: £") + str(basic_nic))
        print(("NIC @ 2%: £") + str(higher_nic))
        print("Your net salary is: £" + str(take_home_pay))

else:
    b_tax_tot = int(basic_pay * basic_txr)
    h_tax_tot = int(higher_pay * higher_txr)
    add_pay = int(annual_salary - (higher_pay + basic_pay + p_allow))
    a_tax_tot = int(add_pay * add_txr)
    basic_nic = int((nic_base - nic_floor) * basic_nic_rt)
    higher_nic = int((annual_salary - nic_base) * higher_nic_rt)
    total_tax = b_tax_tot + h_tax_tot + a_tax_tot
    total_nic = basic_nic + higher_nic
    take_home_pay = int(annual_salary - (total_tax + total_nic))
    print("Personal Allowance: £" + str(p_allow))
    print("Basic-rate pay: £" + str(basic_pay))
    print("Higher-rate pay: £" + str(higher_pay))
    print("Additional-rate pay: £" + str(add_pay))
    print("Basic-rate tax @ 20%: £" + str(b_tax_tot))
    print("Higher-rate tax @ 40%: £" + str(h_tax_tot))
    print("Additional-rate tax @ 45%: £" + str(a_tax_tot))
    print(("NIC @ 12%: £") + str(basic_nic))
    print(("NIC @ 2%: £") + str(higher_nic))
    print("Your net salary is: £" + str(take_home_pay))
