def usd_to_uah(amount):
    exchange_rate = 38.0775
    return amount * exchange_rate

def uah_to_usd(amount):
    exchange_rate = 38.1920
    return amount / exchange_rate

usd_amount =100      #   Вкажіть свою суму доллари
converted_to_uah = usd_to_uah(usd_amount)
print(f"{usd_amount} доларів = {converted_to_uah:.2f} гривень")


#uah_amount = 3800   #Вкажіть свою суму гривні
#converted_to_usd = uah_to_usd(uah_amount)
#print(f"{uah_amount} гривень = {converted_to_usd:.2f} доларів")