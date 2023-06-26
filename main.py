import subprocess

corp_prefixes = ["010 ","044", "013", "033"]
home_prefixes = ["004", "003", "044", "014", "141"]
cuit_cuil_prefixes = ["20", "23", "24", "25", "26", "27", "30", "33", "34"]

def fibertel() -> None:
    """
    Generates Fibertel Home Networks wordlist
    """
    print("[+] Creating dictionaries for home networks...")
    fibertel = open("fibertel.txt", "a")

    for prefix in home_prefixes:
        for i in range (1000000, 50000000):
            fibertel.write('{0:03d}{1:08d}'.format(int(prefix), int(i)))
            fibertel.write('{0:03d}{1:07d}'.format(int(prefix), int(i))) # Certain confution exists about if the DNI is the whole number or the first 7 digits, so I will double the posibilities.
    fibertel.close()
    print("Done")


def fibercorp() -> None:
    print("[+] Creating dictionaries for corpotative networks...")
    fibercorp = open("fibercorp.txt", "a")
    
    for prefix in corp_prefixes:
        for prefix_ in cuit_cuil_prefixes:
            for i in range (0, 100000):
                fibercorp.write('{0:03d}{1:2d}{2:05d}'.format(int(prefix), int(prefix_), int(i)))
                fibercorp.write('{0:03d}{1:2d}{2:09d}'.format(int(prefix), int(prefix_), int(i))) #the same confurion apperares here so I will duplicate again.
    fibercorp.close()
    print("Done")

def main():
    fibertel()
    fibercorp()

    

if __name__ == '__main__':
    main()
