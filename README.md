# CSR-automagically
CSR automation saves time and effort by creating certificates signing requests in one shot for multiple appliances
This tool is intended for saving time and efforts dedicated for generating Certificate Signing Requests for Secure Network Analytics, if SNA GUI is used this involves multiple clicks and typing in information for the required input fields.

 CSR Manufacturing tool generates all the CSR for all the appliances part of the SNA landscape in one shot 
It is been briefly tested on SNA 7.4.1 and 7.5.1.
The performed testing is not exhaustive, therefore there might be some errors here there.

Input files:
 CSR_infofile.csv, this file must be filled out with CSR related info, prior running the script.
Excel can be used for filing out the info and then save the file as CSR_infofile.csv.  DO NOT CHANGE this filename. There are means to upload this file explained in a few paragraph below.
 

CommonName.cnf this file is used for ssl configuration and has been adjusted to fit SNA ssl/tsl certs requirement. As a side note this tool can be used to generate CSRs for virtually any technology that employs the use of ssl/tsl certificates. This file must be placed under the same directory as the two python scripts: CSR_ONE_SHOT_GUI.py and Function_test.py.



How to proceed:

Download the package and extract the files from the archive.

On the local environment there should be installed python3 with csv, numpy pathlib, os, glob, time shutil, sys, flask, subprocess, zipfile, these are the modules specified at the top of the two python scripts: Function_test.py and CSR_ONE_SHOT_GUI.py

Run CSR_ONE_SHOT_GUI.py then open a browser and access:

http://127.0.0.1:5000

Upload the CSR_infofile.csv
give it a bit of time and then you’ll be presented with your CSR archive : csr_files.zip available to download.


<img width="540" height="741" alt="image" src="https://github.com/user-attachments/assets/262bc1d1-3d91-423a-be2e-848017a08ae6" />
