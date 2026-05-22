#EduBreachTools
#2026

import json
import sys
import os
import time

R = "\033[1;31m"  
G = "\033[1;32m"  
Y = "\033[1;33m"  
B = "\033[1;34m"  
M = "\033[1;35m"  
C = "\033[1;36m"  
W = "\033[1;37m"  
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'siswa.json')

def hitung_total_siswa():
    file_path = get_file_path()
    if not os.path.exists(file_path):
        return 0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return len(data)
    except Exception:
        return 0

def procces_loading():
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    print(f"{C}▶ PROCCESING DATABASE...{RESET}")
    
    for i in range(1, 11):
        for frame in frames:
            percent = i * 10
            sys.stdout.write(f"\r {Y}{frame}{W} Membaca Indeks Kebocoran: {G}{percent}%{RESET}")
            sys.stdout.flush()
            time.sleep(0.015)
            
    sys.stdout.write("\r\033[K")      
    sys.stdout.write("\033[A\033[K")  
    sys.stdout.flush()

def print_banner(total_siswa):

    print(f"{R}     ______ {RESET}")
    print(f"{R}  .-\"      \"-.   {Y} ___    _         {RESET}")
    print(f"{R} /            \\  {Y}| __|__| |_  _    {RESET}")
    print(f"{R}|              | {Y}| _|/ _` | || |   {RESET}")
    print(f"{R}|,  .-.  .-.  ,| {Y}|___\\__,_|\\_,_|   {RESET}")
    print(f"{R}| )(__/  \\__)( | {C} ___                    _     {RESET}")
    print(f"{R}|/     /\\     \\| {C}| _ )_ _ ___ __ _  ___| |_   {RESET}")
    print(f"{R}(_     ^^     _) {C}| _ \\ '_/ -_) _` |/ _| ' \\  {RESET}")
    print(f"{R} \\__|IIIIII|__/  {C}|___/_| \\___\\__,_|\\__|_||_| {RESET}")
    print(f"{R}  | \\IIIIII/ |{RESET}")
    print(f"{R}   \\________/{RESET}")
    
    print("")
    print(f" {C}◆{W} Creator        : {Y}AldoOfficialR{RESET}")
    print(f" {C}◆{W} GitHub         : {B}https://github.com/aldoofficialrphie{RESET}")
    print(f" {C}◆{W} Instagram      : {M}https://instagram.com/aldxyzv{RESET}")
    print(f" {C}◆{W} Total Database : {G}{total_siswa:,} Data Siswa Terindeks{RESET}")
    print("")

def cari_siswa(query_nama):
    file_path = get_file_path()
    if not os.path.exists(file_path):
        return {"error": f"File '{file_path}' tidak ditemukan."}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data_siswa = json.load(file)
    except json.JSONDecodeError:
        return {"error": "Format database 'siswa.json' rusak."}
    
    query_nama = query_nama.strip().upper()
    if not query_nama:
        return []
        
    return [s for s in data_siswa if query_nama in s.get('nama', '').upper()]

def main_interactive():
    while True:
        clear_screen()
        total_siswa = hitung_total_siswa()
        print_banner(total_siswa)
        
        print(f"{W} Masukkan nama target {Y}(ketik 'exit' untuk keluar){W}{RESET}")
        query = input(f"{C} EduBreach ❯ {RESET}").strip()
        
        if query.lower() == 'exit':
            print(f"\n{R}● Sesi EduBreach ditutup. Sampai jumpa.{RESET}")
            break
            
        if not query:
            print(f"\n{R}✗ Input tidak boleh kosong!{RESET}")
            time.sleep(1.2)
            continue
            
        print("") 
        procces_loading() 
        
        hasil = cari_siswa(query)
        
        if isinstance(hasil, dict) and "error" in hasil:
            print(f"{R}[ ERROR ] {W}{hasil['error']}{RESET}\n")
        elif not hasil:
            print(f"{R}[ TIDAK DITEMUKAN ]{RESET}")
            print(f"{W} Data '{Y}{query}{W}' tidak terindeks dalam database kebocoran.{RESET}\n")
        else:
            print(f"{G}[ TERDETEKSI ] Ditemukan {C}{len(hasil)}{G} data yang cocok:{RESET}\n")
            
            for index, siswa in enumerate(hasil, 1):
                print(f"{Y}━ DATA SISWA #{index} ━━━━━{RESET}")
                
                keys_clean = [k.replace('_', ' ').upper() for k in siswa.keys()]
                max_pad = max(len(k) for k in keys_clean) if keys_clean else 15
                
                for key, val in siswa.items():
                    key_display = key.replace('_', ' ').upper()
                    print(f"  {C}•{W} {key_display:<{max_pad}} : {G}{val}{RESET}")
                print("")
                
        print(f"{M} Tekan [Enter] untuk mencari kembali...{RESET}")
        input()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nama = sys.argv[1]
        hasil = cari_siswa(nama)
        print(json.dumps(hasil))
    else:
        main_interactive()