# -*- coding:utf-8 -*-
import sys
from pykd import *
import string
import os

pagesize = 0x1000
looptime = 0x100000000 / 0x1000

def processInfo():
    base_dir = 'E:\\'
    temp_filepath = os.path.join(base_dir, "Temp_memory")
    whole_filepath = os.path.join(base_dir, "Xp_whole_memory")
    zero_filepath = os.path.join(base_dir, "zero_memory")
    mark_missing_filePath = os.path.join(base_dir, "mark_missing_address.txt")
    mark_exist_filePath = os.path.join(base_dir, "mark_exist_address.txt")

    whole_file = open(whole_filepath,'wb+')
    zero_file = open(zero_filepath, 'rb')
    zero_file_read = zero_file.read()
    mark_missing_open=open(mark_missing_filePath,"w")
    mark_exist_open=open(mark_exist_filePath,"w")

    missingCount=0
    existCount=0

    for i in range(looptime):
        commandstr_dd = "dd " + hex(i * pagesize)[0:10] + " " + hex(i * pagesize + 1)[0:10]
        result = dbgCommand(commandstr_dd)
        if(result[10:11] == '?'):
            whole_file.write(zero_file_read)
            missingCount=missingCount+1
            mark_missing_open.write(str(missingCount) + "\t: start-> "+ strConvert(str(hex(i * pagesize)[0:10])) +"\tend-> "+ strConvert(str(hex((i+1) * pagesize - 1)[0:10]))+ "\t(Page\t"+ str(i+1) +")\n")
        else:
            commandstr = ".writemem " + temp_filepath + " " + hex(i * pagesize)[0:10] + " " + hex((i+1) * pagesize-1)[0:10]
            dbgCommand(commandstr)
            temp_file = open(temp_filepath,'rb')
            temp_file_read = temp_file.read()
            existCount=existCount+1
            mark_exist_open.write(str(existCount) + "\t: start-> "+ strConvert(str(hex(i * pagesize)[0:10])) +"\tend-> "+ strConvert(str(hex((i+1) * pagesize - 1)[0:10]))+ "\t(Page\t"+ str(i+1) +")\n")
            whole_file.write(temp_file_read)
            temp_file.close()

    mark_missing_open.write("the percent of the missing page :"+ str(missingCount) +"/"+ str(looptime)+"="+str(round(100*missingCount/looptime,2))+"%")
    mark_exist_open.write("the percent of the exist page :"+ str(existCount) +"/"+ str(looptime)+"="+str(round(100*existCount/looptime,2))+"%")
    mark_missing_open.close()
    mark_exist_open.close()
    whole_file.close()

def strConvert(addrString):
    temp=""
    i=0
    addrSlice=addrString.split("x")
    addrPart=addrSlice[1]
    while i< (8-len(addrPart)):
        temp=temp+"0"
        i=i+1
    return "0x"+ temp + addrPart

def run():

    if not isWindbgExt():
        if not loadDump( sys.argv[1] ):
            dprintln( sys.argv[1] + " - load failed" )
            return

    if not isKernelDebugging():
        dprintln( "not a kernel debugging" )
        return

    processInfo()

if __name__ == "__main__":
    run()
