# %%
def start_washing(eco=False):
    # Step 1 - Pump water for 10 minutes
    print("Pumping water -> 10 minutes")
    pump_water(duration=10, energy=5 if not eco else 5)
    
    # Step 2 - Spin for 5 minutes
    print("Spinning -> 5 minutes")
    spin(duration=5, energy=15 if not eco else 15)
    
    # Step 3 - Heat water for 20 minutes
    print("Heating water -> 20 minutes")
    heat_water(duration=20, energy=1300 if not eco else 900)
    
    # Step 4 - Rinse for 15 minutes
    print("Rinsing -> 15 minutes")
    rinse(duration=15, energy=80 if not eco else 40)
    
    # Step 5 - Spin for 40 minutes
    print("Spinning -> 40 minutes")
    spin(duration=40, energy=500 if not eco else 800)
