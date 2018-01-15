#!/usr/bin/env python
#Created by: Anthonys.io
import csv
import urllib2
import commands
import subprocess
import os;
import sys;
import re;
import csv;
import time;
import shutil;
import datetime;
import errno;
import fileinput;

#filter words go below
filterr = ['MS811 ', 'chu'] 

#====================================
filtered = [x.strip(' ') for x in filterr] #strips out white space in list
now = datetime.datetime.now()
currentdate = now.strftime("%Y-%m-%d %H:%M")
path = "report_page"
ext = ".html"
filenames = ['> 1', '> 2', '> 3', '> 4', '> 5', '> 6', '> 7', '> 8', '> 9', '> 10']
start_line = '<td><div style=\"display: inline-block; width: 300px; word-wrap: break-word\">'
end_line = 'height=\"400\"></a></div></td></tr></div>'
path_page = 1 #first page
path_max = 4 #last page
catfile = "catfile.txt" #auto remove
sleep_time = 0
timeout = float(sleep_time)
now = datetime.datetime.now()
directory = ('Eyewit_ext '+now.strftime("%Y-%m-%d %H:%M:%S"))
print('\x1b[6;30;42m' + '=============EyeWitness Filtration=============' + '\x1b[0m')
print('\x1b[6;30;42m' + 'How to: Place script inside main directory with report_page files/screens/source.' + '\x1b[0m')
print('\x1b[6;30;42m' + 'Description: Script will make a directory, and place the corresponding reponse code with their HTML file, will also filter results with tags.' + '\x1b[0m')
print('\x1b[6;30;42m' + '' + '\x1b[0m')
print('Start Page:'+'\x1b[6;30;42m' + str(path_page) + '\x1b[0m')
print('End Page:'+'\x1b[6;30;42m' + str(path_max) + '\x1b[0m')
print('Filtered Words:'+'\x1b[6;30;42m' + ', '.join(filtered) + '\x1b[0m')
print('Writing to directory:'+'\x1b[6;30;42m' + directory +'/'+'\x1b[0m')
print('\x1b[6;30;42m' + '' + '\x1b[0m')
raw_input("Press Enter to continue...")
print('\x1b[6;30;42m' + '' + '\x1b[0m')
os.mkdir(directory)
try:
	shutil.copy('report.html', 'report_page1.html')
except:
	print "report file already changed, moving on.."
for i in range(path_page, path_max+1):
	fullpath = path+str(i)+ext
	print(fullpath)
	cmd = ("cat " +fullpath+"")
	output = commands.getoutput(cmd)
	time.sleep(timeout)
	with open(catfile, 'w') as f:
		f.write(output)
		f.close()
	with open(catfile, 'r') as f:
		lines = f.read().splitlines()
	state = 'default'
	for line in lines:
		line = line.strip()
		if state == 'default':
			if line == start_line:
				state = 'important'
				important_rows = []
				write = True
		elif state == 'important':
			if line != end_line:
				for filt in filtered:
					if filt in line:
						write = False
				important_rows.append(line)
				for filename in filenames:
					if filename in line:
						if '> 1' in line:
							output_file = directory+"/1xx" + '.html'
						if '> 2' in line:
							output_file = directory+"/2xx" + '.html'
						if '> 3' in line:
							output_file = directory+"/3xx" + '.html'
						if '> 4' in line:
							output_file = directory+"/4xx" + '.html'
						if '> 5' in line:
							output_file = directory+"/5xx" + '.html'
						if '> 6' in line:
							output_file = directory+"/6xx" + '.html'
						if '> 7' in line:
							output_file = directory+"/7xx" + '.html'
						if '> 8' in line:
							output_file = directory+"/8xx" + '.html'
						if '> 9' in line:
							output_file = directory+"/9xx" + '.html'
			else:
				if write:
					with open(output_file,'a') as f:
						f.write('<table border=\"1\"><tr><th>Web Request Info</th><th>Web Screenshot</th></tr><tr>')
						f.write('<td><div style=\"display: inline-block; width: 300px; word-wrap: break-word\">' + '\n')
						for row in important_rows:
							f.write(row + '\n')
						f.write('height=\"400\"></a></div></td></tr></div>' + '\n')
						f.write('<tr>' + '\n')
						f.write('</center><br></body></html>')
						f.write('\n'+'\n')
				state = 'default'
	os.remove(catfile)
#THE CLEAN UP=====================================
os.chdir(directory)
cmd = ("grep -rl 'screens/' ./ | xargs sed -i 's/screens\//..\/screens\//g'")
cmd1 = ("grep -rl 'source/' ./ | xargs sed -i 's/source\//..\/source\//g'")
output = commands.getoutput(cmd)
output = commands.getoutput(cmd1)
print('\x1b[6;30;42m' + 'FINISHED' + '\x1b[0m')
f.close()
