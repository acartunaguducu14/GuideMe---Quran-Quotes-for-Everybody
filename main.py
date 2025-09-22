#!/usr/bin/env python3


import requests
import random

def get_all_quotes():
    url = "https://quranquotes.vercel.app/api/getAll"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        print("Error fetching quotes")
        return []

def get_random_quote(quotes):
    return random.choice(quotes)

def main():
    quotes = get_all_quotes()
    if not quotes:
        print("No quotes available :/")
        return
    
    quote = get_random_quote(quotes)

    text = quote.get('quranQuote', "No quote text found")
    reference = quote.get('reference', "Unknown reference")

    try:
        surah_ayah = reference.split()[-1]
        surah, ayah = surah_ayah.split(':')
    except Exception:
        surah, ayah = "Unknown Surah", "Unknown Ayah"
    
    
    print("""
          
          
          ⠀⠀⠀⠀⠐⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠃⠀⠀⠀⠀⢀⠀⠀⠀⠘⣿⣿⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⠀⣀⣠⡴⠖⠋⠀⠀⠀⠀⢿⣿⠻⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠴⠞⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⠋⠉⣠⡆⠰⡇⠸⡇⠀⠀⠀⠀⠀⠀⠀⠸⣿⡇⠀⠀
⠀⠀⠀⠀⠀⢠⣤⡈⠀⠀⠀⠀⢻⡇⢀⣷⣀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⠀⠀
⠀⠀⠀⠀⠀⢸⡿⠗⠀⠀⠀⠀⠈⠛⠛⡉⠛⠁⠀⠀⠀⣧⠀⠀⠀⠀⢻⣿⠀⠀
⠀⠀⠀⠴⠞⠉⠀⠀⠀⡀⠀⠀⠀⠀⢀⣿⡄⠀⠀⠀⠸⣿⣧⠀⠀⠀⢸⣿⡀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⡇⠀⠀⠀⠀⠈⣿⣧⠀⠀⠀⠀⢻⣿⠷⠀⠀⠈⣿⡇⠀
⠀⠀⠀⠀⠀⠀⢰⡿⢻⡇⠀⠀⠀⠀⠀⢿⣿⠀⠀⠀⠀⠘⣿⡆⠀⠀⠀⣿⣧⠀
⢠⡆⠀⠀⠀⠀⣾⠃⣾⡇⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⠀⢿⣿⡀⠀⠀⢸⣿⠀
⢸⡇⠀⠀⠀⢠⡿⠀⣿⠀⠀⠀⠀⠀⠀⠈⣿⣇⠀⠀⠀⠀⠘⣿⣇⠀⠀⠘⣿⡄
⢸⣧⠀⠀⠀⢸⡇⠀⣿⡀⠀⠀⠀⠀⠀⢰⣿⣿⡄⠀⠀⠀⠀⢹⡟⠀⠀⠀⣿⡇
⠈⣿⡄⠀⢀⣿⠇⠀⣿⣧⡀⠀⠀⠀⣠⣿⠋⣿⣿⣦⣀⣀⣠⣾⡇⠀⠀⠀⢿⡇
⠀⢻⣿⣶⣾⡿⠀⠀⠹⣿⣿⣶⣶⣿⣿⠋⠀⠈⠻⣿⣿⣿⡿⠟⠀⠀⠀⠀⢸⡇
⠀⠀⠙⠛⠋⠀⠀⠀⠀⠈⠛⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀
          
          
          """)
    
    print(f"\n\"{text}\"")
    print(f"- Surah {surah}, Ayah {ayah}")

if __name__ == "__main__":
    main()
