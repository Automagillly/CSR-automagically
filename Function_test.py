#!/usr/bin/python3

###READ BEFORE YOU RUN:
###CommonName.cnf MUST BE IN PATH 
###CSR_infofile.csv=>> THIS IS THE INPUT FILE MUST BE IN PATH
###SCRIPT Function_test.py MUST BE IN PATH
#####REMOVE ALL  FOLDERS AND FILE REMINICENSES OF THE PREVIOUS RUN OF THE CSR MANUFACTURING TOOL 
####THIS SCRIPT IS BARE MINUMUM 
import csv
import numpy as np
from pathlib import Path
import os
import glob
import shutil
import time
import sys


src = "CommonName.cnf" # this path is usually pointing to the current directory, double check though before runing the script
#src = "./generic_conf_file.cnf" # this path is usually pointing to the current directory, double check though before runing the script
myCmd = "openssl genrsa -out privkey.pem 8192" # for ease of use this is hard coded, it can be adjusted to ask for customer input for key lenght
CSR = "./CSR"

## for improvements organize code based on functions and call each function as needed
## treat errors ex: input csv file no being present in the path
##                  check the presence of generic_conf_file.cnf


file = open("CSR_infofile.csv", "r") ## input file with CSR required details needs to be in .csv format
#data = list(csv.reader(file, delimiter=","))
intermed = np.delete((list(csv.reader(file, delimiter=","))),[0,1], axis=0)
measure = len(intermed)


print(measure)

def create_dirs_add_open_cnf_file(measure):
    os.mkdir(CSR) 
    for n in range(measure):
        ComoomN = intermed[n][0]
        CName = ComoomN.split(".")[0]
        path = ("./" + CName)
    
        print(CName)
        print(path)

        os.mkdir(path)                     ####creates directories for each appliance named based on each appliance FQDN
        dst = (path + "/" +  CName + ".cnf")
        print(dst)
        shutil.copy(src,dst)               ###copy openssl.cnf file to each appliance's directory 


def key_cert_creation_command(myCmd):
    path = "./private_key"
    os.mkdir(path) 
    
    os.system(myCmd)
    src = "./privkey.pem"
    shutil.move(src,path) 


def customize_cnf_file_per_csv_infle_input(measure):
    for n in range(measure):
        ComoomN = intermed[n][0]
        CName = ComoomN.split(".")[0]
        dst = ("./" + CName + "/" +  CName + ".cnf")
        with open(dst, "r+") as file:
            contents = file.read()
            contents = contents.replace("$CommonName", intermed[n][0]) 
            contents = contents.replace("$CountryName", intermed[n][1])
            contents = contents.replace("$State", intermed[n][2])
            contents = contents.replace("$LocalityName", intermed[n][3])
            contents = contents.replace("$OrganizationName", intermed[n][4])
            contents = contents.replace("$OrganizationUnit", intermed[n][5]) 
            contents = contents.replace("$emailaddress", intermed[n][7])
            contents = contents.replace("$IpAdress", intermed[n][6])
            print(intermed[n][0]+".cmf file has been created" )
    
            file.seek(0)       
            file.write(contents)
            file.truncate() 
     
        command = str("openssl  req -new  -config " + dst + " -key ./private_key/privkey.pem -out " + CSR + "/" + intermed[n][0] + ".csr") 
        print(command)
        os.system(command) 
        
 

create_dirs_add_open_cnf_file(measure)
key_cert_creation_command(myCmd)
customize_cnf_file_per_csv_infle_input(measure)
