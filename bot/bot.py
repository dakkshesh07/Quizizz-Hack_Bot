#!/usr/bin/env python3
import os, time, json, requests, sys, random, string, tkinter, subprocess, tempfile
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pyperclip
from time import sleep
#-------------------------------------------------------------------------#


#("Quizizz Hack Script by dakkshesh")
#No rebuild allowed
#To contact me DM me on discord "dakkshesh#0517"

print("   ____        _     _           _    _            _       _____           _       _   ")
print("  / __ \      (_)   (_)         | |  | |          | |     / ____|         (_)     | |  ")
print(" | |  | |_   _ _ _____ ________ | |__| | __ _  ___| | __ | (___   ___ _ __ _ _ __ | |_ ")
print(" | |  | | | | | |_  / |_  /_  / |  __  |/ _` |/ __| |/ /  \___ \ / __| '__| | '_ \| __|")
print(" | |__| | |_| | |/ /| |/ / / /  | |  | | (_| | (__|   <   ____) | (__| |  | | |_) | |_ ")
print("  \___\_\\__,_|_/___|_/___/___| |_|  |_|\__,_|\___|_|\_\ |_____/ \___|_|  |_| .__/ \__|")
print("                                                                            | |        ")
print("                                                                            |_|        ")

print("_  _ ____ ___  ____    ___  _   _    ___  ____ _  _ _  _ ____ _  _ ____ ____ _  _")
print("|\/| |__| |  \ |___    |__]  \_/     |  \ |__| |_/  |_/  [__  |__| |___ [__  |__|")
print("|  | |  | |__/ |___    |__]   |      |__/ |  | | \_ | \_ ___] |  | |___ ___] |  |")
print("                                                                                 ")

print("please make this window fullscreen to make this script work")

input("press any key to start the bot....")

#print("░░░░░░░░░░░▓██████▓▓▓▓▓██████▓░░░░░░░░░░░")
#print("░░░░░░░░░████▒░░░░░░░░░░░░░▓████░░░░░░░░░")
#print("░░░░░░░███▓░░░░░░░░░░░░░░░░░░░▓██▒░░░░░░░")
#print("░░░░░░██▓░░░░░░░░░░░░░░░░░░░░░░░██▓░░░░░░")
#print("░░░░▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░")
#print("░░░░██░░░▒▒▒░░░░░░░░░░░░░░░▒▓███▓░░█▓░░░░")
#print("░░░██░░▓▓▓▓▓▓▓▒░░░░░░░░░░▒▓███████▓░█▒░░░")
#print("░░██░▒███████▓▒▒░░░░░░░░▒██████████▓▓█░░░")
#print("░░█░▒██████████▓░░░░░░░▒██████▓▒▒▓██░██░░")
#print("░██░██░░░░░▓▓▓███▒░░░░░█████░░░░░░░██░█░░")
#print("░█░██░░░░░░░░▓▓██▓░░░░░░██▒░░░░░░░░░▓░██░")
#print("▒█░▓░░░░░░░░░░▓██░░░░░░█▓░░░░░░░░░░░░░▓█░")
#print("▓█░░░░░░░░░░░░░░██░░░░█▓░░░░░▒▒▒░░░░▒░░█░")
#print("█▓░░░░░░░▓███▓▓░░▒█░░░█░░░▒██▓▓▓█░░░░▓░█░")
#print("█▒▒░░░░░█▓░▒▒▒▓█▓░▒▒░░▓░░█▓▓▓██▓▓█░░░▓░█▒")
#print("█░▒▒░░░█▓▓████▓░█▒░▒░░▓░█▓███████▓▓░░█░█▓")
#print("█░░▓░░▒█████████▓█░▒░░▒░█▓███████▒███░░█▓")
#print("█░░█▒▓█▓█████▓▓▓█░░▒░░▒░░█▓▒▒▒░░░▒███░░▓█")
#print("█░░▒███▓▓▓▓▓▓▓▒░░░░▒░░▒░░░░▓▓▓▓▓▓▒░▒██░░█")
#print("█▒░▓▓░░░░░░░░░░░░░░▒░░▒▒░░░░░░░░░░░░░█▓░█")
#print("█▓░▒░░░░░░░░░░░░░░░▒░░░▒░░░░░░░░░░░░░░▓░█")
#print("█▓░░░░░░░░░░░░░░░░░▒░░░▒░░░░░░░░░░░░░░▒░█")
#print("▓█░░░░░░░░░░░░░░▒░░░░░░░░░█░░░░░░░░░░░░░█")
#print("▓█░░░░░░░░░░░░░█░░░░░░░░░░▒█░░░░░░░░░░░░█")
#print("▓█░░░░░░░░░░░░█▓░░░░░░░░░░░██░░░░░░░░░▓░█")
#print("▓█░░░░░░░░░░▓██▒░▓░░░░░░░█░▓▓██░░░░░░░█░█")
#print("▒█░▒░░░░░░▓██░░█░██▓░░░░███▓░░██▓░░░░█▓░█")
#print("░█░░█░░░▓██▓░░░▒▓▒███▓▓██░▒░░░░░██▓▓█▓░░█")
#print("░█░░░█████░░░░░░░░███████░░░░░░░░████░▓░█")
#print("░█▒░░░▓███▒░░░░░░████▒▓███▒░░░░░▓███░░▓░█")
#print("░█▓░░░▓▒███▒░▒▓█████▒░░█████████████░▒▓██")
#print("░██░░░░▓░██████████▒░░░░█████████▒█░░▓█▓█")
#print("░▓█░░░░░▓░██████████████████████▒▓█░░█░▒█")
#print("░▒█░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░▒█░░██░█▓")
#print("░░█░░░░░░██░░░░░░░░░░░░░░░░░░░░▓█▒░▒█░░█▓")
#print("░░█▓░▒░░░░█████████▓▓▓▓▓██████▓▓█░░█▒░░█░")
#print("░░▓█░▒▓░░░▒█░░▒▒▓▓▓██████▒░░░░░█░░█▓░░▒█░")
#print("░░░█░░▓█░░░▓▓░░░░░░░▓███▒░░░░░▓▓░▒█░░░██░")
#print("░░░██░░██░░░█▒░░░░░░░███░░░░░░█░░█░░░░█▒░")
#print("░░░░▒█▒░░██░░░█░░░░░████▓░░░▒▓░▓▓░░░▓█░░░")
#print("░░░░░▓█▓░░▓▓░░░█░░░░█████░░░░░░▓░░░▓█▒░░░")
#print("░░░░░░▓██░░▒░░░░▓░░░▓███▓░░░░░▓░░░▓█▓░░░░")
#print("░░░░░░░░██▒░░░░░░░░░▒███▓░░░░▒░░░██▓░░░░░")
#print("░░░░░░░░░███░░░░░░░░░███▒░░░░░░░██▒░░░░░░")
#print("░░░░░░░░░░▒██▓░░░░░░░███░░░░░░▓██░░░░░░░░")
#print("░░░░░░░░░░░░▓██▓░░░░░▓██░░░░░██▓░░░░░░░░░")
#print("░░░░░░░░░░░░░░███▒░░░░█▒░░▒███░░░░░░░░░░░")
#print("░░░░░░░░░░░░░░░░████▓▓█▓████░░░░░░░░░░░░░")


print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMWX0OkOOxc,'';xKNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkoc:,'...''''.''',;::cox0XWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMWN0dc,..    .   ... .........  ..;lx0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNOl,.   ....      .         .......  ..,lx0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk:.  .....                        ....  ..':lx0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNk;........                            ... .. .',:oONWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c...........                             ....  ...,:kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,........ ..                               ....   ..;l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXd'...........                                 .....  .,;lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd,.''.........                                 .....  ..;:xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk:'',''........                                  ..... ..,:lKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0l;;:,'.........                                   .......,;oONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk:,::,'............            .  .... .           .......;:lOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd;;c:,'............... ... ... ......  .            ......,:lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd:ll;,'.........   ......   .. ..  ... ..            ......:dOXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXdcol;,'.........    .....   .. ..  . .. ..   .       ......;x0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXdloc;,'.........   ....... .....   ....               .....'o0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNxloc;,'.......... ...                                 ......:OKXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNxclc;,'.............                                  ......;kKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk:cc;,''........                                      ......;x0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk::c:,,'........                                      ......,dKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKc;::;;,'.......                                      .......l0NNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo::cc;,'.......                                       .....'cxXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMXkdlc:clc,.........                               ........'',,;clol;:kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:..;ccc:,,''............                   ........'''',,,,,;clol'..lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0l;:oddolc:;,'...........              ...........''''',,,;;;:clo:',.oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXocdOxdoc:;,'...............    ...................''''',,;:ccldo::c;lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdcxOxoc:;,,'.............................................';lxdoo:';:lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("(MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx:xkocc:;,,'...........      ..............              .'c::l;. .:xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKoxkl:;,'''.....               ..........                    .l,  .:OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxl::loo,.                                                 .lx,..;xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXk:,xXKl.                       ...                      .c0x',d0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNOcoKKx'                ..  ......                      'd0xcxXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXxd0KOl.           ... ....''.....                    .ckOxxXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0xk0Oxc.   ............ .;:;;,...        ......     .:kOxxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXK0Okdc,.. ...........',l:;;'..            .     ..cx0kkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXkxxdooc;''.......'''',,,'..                 ...'cdkxlkWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMNOdoolcc:;,,,,,,,,,''.......                  ...';;,c0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOc;,,,'''''','','''........                     ..'oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo;,,''''.';;,'''...........                   ..':xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxc,,'','.'::'............                    ...'l0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOo:;,,,'.';c;'............                  ....,dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXNNxc;,,,''';c:,.'..........          ..     ....'c0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMWXd;dXKd;,,,''';::;.............       ....   ......;dXMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMWO;. :KKko;,'''';;;:'......'.......    ... ..  .....,;':0WWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0,   ,kOxdc;,''';;,:,....''.........    .  ..  ....,:'  ,OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXo.   .,:locc:;,',;,,;,';;;....     ..         ....';:.   :KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXkl'    .;;;cccc:',:,.,::,'....               .....';:'    'xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWKxoo;.    ',',:llc:;:;',::.......        ..    ....',;'     ,lOXNNWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXXK0Odcll:,..  ..'',cllcccc::;;,'...         ..........',;'     .;coxxxOKXNWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNX0kkOxo::::,,'...  ...,llc:cll;..,;,..        ... ......',;,.    .,::codkdok0KXNNNNNNNNWWMMWWMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNWWNXKOdcxOo:,,;,,''''...  ..;ll:;:c;...'''.       ....   ....,;;.    .,::::codo:;::clddoccox0K00KXNNWWMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNXXKK00Okdlc;':dl;,''''''''''...  .;ll;,,''....''.     .....    ..',,.    .,;:;,;;ld:...''',,,,;lddolldxxOKXWMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMWWNNXK0Okxxdollc::;,'...:dl;,'..'..'''...   .;lc;;,,'.......   .....     ..,'.    .,:;;,,,;ll'......'',:llcccccclodxkOXWNXNMMMMMM")
print("MMMMMMMMMMMMMMMMMWNXK0Okxdoolc::;;,,,,'''.....';clc;'....''....   .;lc;;;,,''...........      .''.     .,:,''',::'..    ..;::,'';;:::clooooxkdkXNNNWMM")
print("MMMMMMMMMMMMWNNX0Oxdolcc:::;;;;,,''.'''..........;ccc;'.........   .,::;,,,,'..........      ....     ..,,'',;c;...... ..';;'..'''',;;:clll::okkxxOXXX")
print("MMMMMMWWNNX0kxdlc:;;;;;;;;;;,,''.....''............'::;'........    .,;;;,,,'......'...      ...     ...''';;;'.........''...''....''',,;;,,cl:'';d00O")
print("MMMMWNK0kdolc::;,,',,;;;;,,,''''...''''''........ ...';;'........    .,;;;,,,'.......       ...       ...',:,.........'...'.....''........';ll;....;lx")
print("WWNXOxdoc:;;;,,,,,,,,,,,,,'''''''''''..................'''.....       .';;,,''...           ...        ..',...............''................;loc,....'")
print("X0kxdlc:;;;;,;,,,,'''''''''''''............................''..        .',,,''....          .         ..... ........,.....'...'..........','.'col:'...")
print("Okxdlc::;;:;;;;,''........''''..........................'...''..        ..,,,''..                              .....''....,............  .','.,cll:,..")


print("Ready To Hack")


#input("press any key to start the hacking.....")


global enabled
def randdelaygen(base,tf):
    if tf==True:
        mult=random.randint(15,50)
        delay=base+mult/10
    else:
        delay=base
    time.sleep(int(delay))
def waitForItem(driver, css, timeout=20):
    WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, css)))



code = input("gamecode>>")

user = input("username>>")

d = DesiredCapabilities.CHROME
d["goog:loggingPrefs"] = { 'performance':'ALL' }
driver = webdriver.Chrome(desired_capabilities=d)

#input("Press any key to start the web automator and java injector")

driver.get("https://quizizz.com/join/")
print("[info] Starting game")
waitForItem(driver,'.check-room-input')
driver.find_element_by_css_selector('.check-room-input').send_keys(code)
driver.find_element_by_css_selector('.check-room-button').click()
waitForItem(driver,'.enter-name-field')
driver.find_element_by_css_selector('.enter-name-field').send_keys(user)
driver.find_element_by_css_selector('.start-game').click()
time.sleep(5)

#import io

#f = io.open("code.txt", mode="r", encoding="utf-8")

#file = f.read()

#pyperclip.copy(file)


with open(os.path.abspath('code.txt'), mode="r", encoding="utf-8") as js_file:
    line = js_file.readline()
    script = ''
    while line:
        script += line 
        line = js_file.readline()

driver.execute_script(script)
sleep(2)
#driver.quit()

print("script injected, HACKED")

print("Program ended, you can close this window")
    
    


