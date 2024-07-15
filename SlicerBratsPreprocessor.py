#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:50:09 2023

@author: useradmin
"""


   
    
    
    


    
    
import sys
import subprocess
import os



def checkFileFound(file):
    try:       
        f = open(file, 'r')
        f.close()
    except IOError:
        print('file not found')

def install(package):
	print(sys.executable)
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', package]) 
	

def main(dirPath, Flair, T1, T1c, T2):
    from brats_toolkit.preprocessor import Preprocessor
    # instantiate
    prep = Preprocessor()
   
    print("assigning files to variable")
    examName = os.path.basename(dirPath)
    t1File = T1
    checkFileFound(t1File)
    
    
    t1cFile = T1c
    checkFileFound(t1cFile)
    
    t2File = T2
    checkFileFound(t2File)
    
    flaFile = Flair
    checkFileFound(flaFile)
    
    print(t1File, t1cFile, t2File, flaFile)
    # define outputs
    outputDir = dirPath+"/output"
    print(outputDir)
    # execute it
    prep.single_preprocess(t1File=t1File, t1cFile=t1cFile, t2File=t2File, flaFile=flaFile, outputFolder=outputDir, mode="gpu", confirm=True, skipUpdate=False, gpuid='0')
 
    

    

if __name__ == "__main__":
 
    if len(sys.argv) < 6:
        print("Usage: BratsPreprocessor <input> <sigma> <output>")
        sys.exit(1)
    print("here is sys executable")
    install('BraTS-Toolkit')    
	
    print("I am here ............................................",sys.argv[0],"...",sys.argv[1],"..flair.", sys.argv[2],".T1.", sys.argv[3],"...T2..", sys.argv[4], "..\nt1c", sys.argv[5], "\nt1c..","\nt2..")
  
    try:
    	main( sys.argv[1], sys.argv[2], sys.argv[3],  sys.argv[4], sys.argv[5])
    	
    except subprocess.CalledProcessError as e:
    	print(f"Command failed with return code {e.returncode}")
   
    print("running complete")



