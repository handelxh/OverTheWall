#-*-coding:utf-8-*-
#python3.3.5
import urllib.request,os,time,platform,shutil
# url='http://www.360kb.com/kb/2_150.html'
url = 'https://gitcafe.com/phnessu4/imouto-host/raw/master/360kb/hosts'
_360kb = urllib.request.urlopen(url)
status = _360kb.code
if platform.uname()[0]=='Windows':
    file = r'c:\windows\system32\drivers\etc\hosts'
else:
    file = r'/etc/hosts'
print('-------------------------------------------')
print('-----                                 -----')
print('-----                                 -----')
if status == 200 :
    html = str(_360kb.read())
    a = html.find('#google hosts')
    b = html.find('#facebook hosts 2015 end')
    # print(a,b,html)
    html = html[a:b]
    html = html.replace('<br />', '').replace('&nbsp;', '').replace('<span>', '').replace('</span>', '').replace('\\n', '\n')
    # print('host :')
    # print(html)
    shutil.copyfile(file, '%s.bak-%s'%(file, time.strftime('%Y%m%d%H%M%S')))
    output = open(file, 'w') 
    output .write(html)
    output .close()
    print('-----             执行成功            -----')
else:
    print('-----            执行失败             -----')
print('-----                                 -----')
print('-----                                 -----')
print('-------------------------------------------')
file = r'./360kb/hosts'
output = open(file,'w')
output.write(html)
output.close()
time.sleep(1)
