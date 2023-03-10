from subprocess import getoutput
from os import system
while(True):
    system("clear")
    print("""------------------ LVM with Python ----------------
            1. Create Physical Volume (PV)
            2. Create Volume Group (VG)
            3. Craete Logical Volume (LV)
            4. Format and Mount a logical Volume
            5. Extend logical Volume size
            6. Display PV
            7. Display VG
            8. Display LV
            0. Exit """)
    ch = int(input("Select option: "))
    if ch==1:
        dev = input("Enter disk or device name: ")
        print(getoutput(f"pvcreate {dev}"))
    elif ch==2:
        pvnames = ''
        while(True):
            pvname = input("Enter PV name: ")
            pvnames += " " + pvname
            check = input("Wnat to give more PV (Y/N): ")
            if check not in ['Y','y']:
                break
        vgname = input("Give a Volume Group name: ")
        print(getoutput(f"vgcreate {vgname} {pvnames}"))
    elif ch==3:
        vgname = input("Enter VG to be used: ")
        lvname = input("Give a name to LV: ")
        size = input("Eneter size you want for LV: ")
        print(getoutput(f"lvcreate --size {size} --name {lvname} {vgname}"))
    elif ch==4:
        lvpath = input("Enter the LV path (/dev/vgname/lvname): ")
        print(getoutput(f"mkfs.ext4 {lvpath}"))
        print("--------------------------------")
        folder = input("Enter the directory path to mount on: ")
        getoutput(f"mount {lvpath} {folder}")
        print("Mounted successfully!")
    elif ch==5:
        lvpath = input("Enter the LV path (/dev/vgname/lvname): ")
        size = input("Enter size you want to add: ")
        print(getoutput(f"lvextend --size +{size} {lvpath}"))
        print("--------------------------------")
        print(getoutput(f"resize2fs {lvpath}"))
    elif ch==6:
        print(getoutput("pvdisplay"))
    elif ch==7:
        print(getoutput("vgdisplay"))
    elif ch==8:
        print(getoutput("lvdisplay"))
    elif ch==0:
        print("Exiting...")
        exit()
    input("Enter to continue...")