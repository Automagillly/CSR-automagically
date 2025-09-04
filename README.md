# CSR-automagically

This tool is intended for saving time and efforts dedicated for generating Certificate Signing Requests.
Use it at your own risk.

Input files:
 CSR_infofile.csv, this file must be filled out with CSR related info, prior running the script.
Excel can be used for filing out the info and then save the file as CSR_infofile.csv.  DO NOT CHANGE this filename. There are means to upload this file explained in a few paragraph below.
 

CommonName.cnf this file is used for ssl configuration and has been adjusted to common ssl/tsl certs requirement. This tool can be used to generate CSRs for virtually any technology that employs the use of ssl/tsl certificates. This file must be placed under the same directory as the two python scripts: CSR_ONE_SHOT_GUI.py and Function_test.py.

 !!!!!  CountryName	StateName	LocalityName are TWO /2 characters long fields by SSL requirements, forr Italy use IT, for France use FR     !!!!!!!

How to proceed:

Download the package and extract the files from the archive.

On the local environment there should be installed python3 with csv, numpy pathlib, os, glob, time shutil, sys, flask, subprocess, zipfile, these are the modules specified at the top of the two python scripts: Function_test.py and CSR_ONE_SHOT_GUI.py

Run Function_test.py if you would like to deal with CLI / linux /MAC promp or Windows cmd

Run CSR_ONE_SHOT_GUI.py if you'd preffer to interact via the a graphical interface,  then open a browser and access:

http://127.0.0.1:5000

Upload the CSR_infofile.csv
give it a bit of time and then you’ll be presented with your CSR archive : csr_files.zip available to download.



