# /usr/bin/env Python
# -*- coding: utf-8 -*-
import sys
from time import sleep
import thread
import os
import signal

"""Maverick
Created By: AfterPacket
www.afterpacket.pw
Description: This will use several methods to create a amplifed  ddos attack against the intended target

License:The MIT License (MIT)
Copyright © 2018 After Packet

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""



print(r"""\
 _______  _______           _______  _______ _________ _______  _       
(       )(  ___  )|\     /|(  ____ \(  ____ )\__   __/(  ____ \| \    /\
| () () || (   ) || )   ( || (    \/| (    )|   ) (   | (    \/|  \  / /
| || || || (___) || |   | || (__    | (____)|   | |   | |      |  (_/ / 
| |(_)| ||  ___  |( (   ) )|  __)   |     __)   | |   | |      |   _ (  
| |   | || (   ) | \ \_/ / | (      | (\ (      | |   | |      |  ( \ \ 
| )   ( || )   ( |  \   /  | (____/\| ) \ \_____) (___| (____/\|  /  \ \
|/     \||/     \|   \_/   (_______/|/   \__/\_______/(_______/|_/    \/


Stresser Tool 	
Created By: AfterPacket wwww.afterpacket.pw
                                                                                        """)


Tsrget=raw_input("Enter IP or Domain Name: " ) 