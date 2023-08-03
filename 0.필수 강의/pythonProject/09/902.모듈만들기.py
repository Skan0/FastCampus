import pay_module

print(pay_module.version)

pay_module.printAuthor()

pay_info = pay_module.Pay("A10201",13000,"2023-08-02")
print(pay_info.get_pay_info())

