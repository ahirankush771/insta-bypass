#!/usr/bin/env python3
import os
import time
import random
import requests
from colorama import init, Fore, Back, Style
from tqdm import tqdm
import threading

init(autoreset=True)

class InstaBypass:
    def __init__(self):
        self.banner()
        self.target_info()
    
    def banner(self):
        os.system('clear')
        print(f"""{Fore.RED}
╔══════════════════════════════════════════════════════════════╗
║  🔥 INSTA-BYPASS v2.0 - PROFESSIONAL BRUTE FORCE 🔥         ║
║  Created by {Fore.YELLOW}Professional Pentester Ankush{Fore.RED} (Ethical Hacker)     ║
╚══════════════════════════════════════════════════════════════╝
        """)
    
    def target_info(self):
        print(f"{Fore.CYAN}[INFO] Enter target details (Educational Demo Only)")
        self.username = input(f"{Fore.GREEN}[+] Target Username: {Fore.WHITE}")
        self.fullname = input(f"{Fore.GREEN}[+] Full Name: {Fore.WHITE}")
        self.email = input(f"{Fore.GREEN}[+] Email/Phone: {Fore.WHITE}")
        self.permission = input(f"{Fore.RED}[!] Type: 'I have permission and am authorized to perform this pentest': {Fore.WHITE}")
        
        if "permission" not in self.permission.lower():
            print(f"{Fore.RED}❌ Authorization required!")
            exit()
        
        print(f"\n{Fore.GREEN}✅ Authorization confirmed!")
        print(f"{Fore.YELLOW}🚀 Starting penetration test...\n")
        time.sleep(2)
        self.attack()
    
    def loading_bar(self, text, duration=2):
        for _ in tqdm(range(100), desc=text, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}'):
            time.sleep(duration/100)
    
    def bypass_stage(self, stage_name, success=True):
        print(f"\n{Fore.MAGENTA}[+] {stage_name}")
        print(f"{Fore.BLUE}    ├─ Scanning... ", end="")
        
        for i in tqdm(range(random.randint(30, 50)), 
                     desc="Bypassing", 
                     bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}'):
            time.sleep(0.05)
        
        if success:
            print(f"{Fore.GREEN}✅ {stage_name} BYPASSED!")
        else:
            print(f"{Fore.RED}❌ Failed")
    
    def attack(self):
        passwords = [
            f"{self.fullname.lower()}123",
            f"{self.username}123",
            f"{self.fullname}2023",
            "password123",
            f"{self.email.split('@')[0]}123",
            "ankush123", "admin123", "qwerty123"
        ]
        
        # Fake bypass stages
        stages = [
            "Instagram Rate Limiter Bypass",
            "Instagram Firewall Bypass", 
            "Terms & Conditions Bypass",
            "CAPTCHA Bypass Module",
            "2FA Bypass Engine",
            "Session Hijacking",
            "API Key Extraction"
        ]
        
        print(f"{Fore.YELLOW}[*] Target Locked: @{self.username}")
        print(f"{Fore.YELLOW}[*] Attack Vectors: {len(stages)}")
        
        # All bypass animations
        for stage in stages:
            self.bypass_stage(stage)
            time.sleep(0.5)
        
        print(f"\n{Fore.RED}{'═'*70}")
        print(f"{Fore.CYAN}🔥 {Fore.WHITE}ALL SECURITY LAYERS BYPASSED!")
        print(f"{Fore.RED}{'═'*70}\n")
        
        # Fake brute force attempts
        print(f"{Fore.GREEN}[+] Starting Brute Force Attack (35 Attempts)")
        print(f"{Fore.YELLOW}[*] Wordlist Size: 1,247,893 passwords")
        
        for attempt in range(1, 36):
            fake_delay = random.uniform(0.3, 0.8)
            time.sleep(fake_delay)
            
            if attempt % 5 == 0:
                print(f"{Fore.BLUE}[{attempt}/35] Testing: {passwords[attempt%len(passwords)]:<15} ", end="")
                self.loading_bar("Checking", 0.1)
                print(f"{Fore.RED}❌ Invalid")
            
            if attempt == 35:
                print(f"\n{Fore.GREEN}[35/35] Testing: {passwords[-1]} ", end="")
                self.loading_bar("Validating", 2)
                print(f"{Fore.GREEN}✅ PASSWORD CONFIRMED!")
        
        # Success screen
        self.success_screen()
    
    def success_screen(self):
        os.system('clear')
        print(f"""{Fore.RED}
╔══════════════════════════════════════════════════════════════╗
║  ✅{Fore.GREEN} PASSWORD SUCCESSFULLY BYPASSED!{Fore.RED}✅                     ║
╠══════════════════════════════════════════════════════════════╣
║  Target: {Fore.YELLOW}@{self.username:<20}║
║  Password: {Fore.GREEN}'{passwords[-1]}'{Fore.RED:<25}║
║  Status: {Fore.GREEN}LOGIN SUCCESSFUL{Fore.RED}                         ║
║                                                             ║
║  {Fore.CYAN}Created by Professional Pentester Ankush{Fore.RED}             ║
╚══════════════════════════════════════════════════════════════╝
        """)
        print(f"{Fore.MAGENTA}\n[*] Session cookies saved to: /sdcard/insta_session.txt")
        print(f"{Fore.YELLOW}[*] Demo complete! Educational purposes only.\n")
        
        input(f"{Fore.CYAN}Press Enter to exit...")

if __name__ == "__main__":
    InstaBypass()
