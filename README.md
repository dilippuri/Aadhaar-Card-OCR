This document for OCR

![Aadhaar to JSON](AadhaarCardOCR1.jpg?raw=true "Aadhaar Card image")

*****************************************************
Problem:
*****************************************************
	Extract information from image of Aadhaar Card by OCR in proper format.
		Information like - 
					Name, Year of Birth, Gender, UID


*****************************************************
Solution:
*****************************************************
	Steps:
		-> Take image
		-> crop to box(which has text in it)
		-> convert into gray scale(mono crome)
		-> give to tesseract
		-> text(output of tesseract)
	Now we will process this text means we will get meaningful information from it.
		-> find name using name database
		-> find gender
		-> find year of birth
		-> find for Aadhar ID(UID)
	for verfication please see aadhar_detail.txt file
	
*****************************************************
Dependent packages
*****************************************************
	-python
	-opencv
	-numpy
	-pytesseract
	-JSON
	-difflib
	-csv
	-PIL
	-SciPy
	-dataparser


*****************************************************
Structure and Usage
*****************************************************
	Directories:
		src-
			which contains code files		
		testcases-
			which contains testing images
		result
			it contains JSON object
			
	Usage:
		python file_name.py [input image]
		Output will be JSON object name
*****************************************************
:100:
