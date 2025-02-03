def total(gallons, sickles, knuts):
    return (gallons * 17 + sickles) * 29 + knuts

coin_list = [100, 50, 25]
coin_dict = {"gallons": 100, "sickles": 50, "knuts": 25}
print(total(*coin_list), "knuts") # * symbol will unpack all values in list
print(total(**coin_dict), "kunts") # ** double symbols for unpacking dict