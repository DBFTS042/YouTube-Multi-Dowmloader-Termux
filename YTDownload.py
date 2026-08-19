#!/usr/bin/env python3

import os
import sys
import shutil
import subprocess

DOWNLOAD_DIR = "/sdcard/Download"

# ---------------------------------------------------------
# Couleurs
# ---------------------------------------------------------

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"


def clear():
    os.system("clear")


def banner():
    print(f"""
{RED}{BOLD}
╔══════════════════════════════════════════════╗
║        YOUTUBE DOWNLOADER - TERMUX          ║
║                                              ║
║       Video • Shorts • Playlists            ║
╚══════════════════════════════════════════════╝
{RESET}
""")


def check_program(program):
    return shutil.which(program) is not None


def check_dependencies():
    missing = []

    if not check_program("yt-dlp"):
        missing.append("yt-dlp")

    if not check_program("ffmpeg"):
        missing.append("ffmpeg")

    if missing:
        print(f"{RED}Dépendances manquantes : {', '.join(missing)}{RESET}")
        print()
        print("Installe-les avec :")
        print()
        print("pkg install ffmpeg -y")
        print('pip install -U "yt-dlp[default]"')
        print()
        sys.exit(1)


def create_download_directory():
    try:
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    except Exception as e:
        print(f"{RED}Impossible d'accéder à {DOWNLOAD_DIR}{RESET}")
        print(e)
        sys.exit(1)


def get_url():
    print()
    print(f"{CYAN}Entrez le lien YouTube :{RESET}")
    print(f"{YELLOW}(vidéo, Short ou playlist){RESET}")
    print()

    while True:
        url = input("> ").strip()

        if not url:
            print(f"{RED}Veuillez entrer un lien.{RESET}")
            continue

        if not (
            "youtube.com" in url
            or "youtu.be" in url
        ):
            print(f"{YELLOW}Attention : ce lien ne semble pas être un lien YouTube.{RESET}")
            confirm = input("Continuer quand même ? [o/N] ").strip().lower()

            if confirm not in ("o", "oui", "y", "yes"):
                continue

        return url


def choose_format():
    print()
    print(f"{BOLD}{WHITE}Choisissez le format :{RESET}")
    print()
    print(f"{GREEN}[1]{RESET} MP3  - Audio")
    print(f"{GREEN}[2]{RESET} MP4  - Vidéo")
    print(f"{GREEN}[3]{RESET} AVI  - Vidéo")
    print(f"{GREEN}[4]{RESET} OGG  - Audio")
    print(f"{GREEN}[5]{RESET} GIF  - Animation")
    print()

    while True:
        choice = input("> ").strip()

        if choice in ("1", "2", "3", "4", "5"):
            return choice

        print(f"{RED}Choix invalide.{RESET}")


def build_command(url, choice):

    # -----------------------------------------------------
    # MP3
    # -----------------------------------------------------
    if choice == "1":
        return [
            "yt-dlp",
            "--ignore-errors",
            "--no-overwrites",
            "--continue",
            "--restrict-filenames",
            "-x",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "-o",
            os.path.join(
                DOWNLOAD_DIR,
                "%(playlist_index&{} - |)s%(title)s [%(id)s].%(ext)s"
            ),
            url
        ]

    # -----------------------------------------------------
    # MP4
    # -----------------------------------------------------
    elif choice == "2":
        return [
            "yt-dlp",
            "--ignore-errors",
            "--no-overwrites",
            "--continue",
            "--restrict-filenames",
            "-f",
            "bv*+ba/b",
            "--merge-output-format",
            "mp4",
            "-o",
            os.path.join(
                DOWNLOAD_DIR,
                "%(playlist_index&{} - |)s%(title)s [%(id)s].%(ext)s"
            ),
            url
        ]

    # -----------------------------------------------------
    # AVI
    # -----------------------------------------------------
    elif choice == "3":
        return [
            "yt-dlp",
            "--ignore-errors",
            "--no-overwrites",
            "--continue",
            "--restrict-filenames",
            "-f",
            "bv*+ba/b",
            "--merge-output-format",
            "mp4",
            "--recode-video",
            "avi",
            "-o",
            os.path.join(
                DOWNLOAD_DIR,
                "%(playlist_index&{} - |)s%(title)s [%(id)s].%(ext)s"
            ),
            url
        ]

    # -----------------------------------------------------
    # OGG
    # -----------------------------------------------------
    elif choice == "4":
        return [
            "yt-dlp",
            "--ignore-errors",
            "--no-overwrites",
            "--continue",
            "--restrict-filenames",
            "-x",
            "--audio-format", "vorbis",
            "--audio-quality", "0",
            "-o",
            os.path.join(
                DOWNLOAD_DIR,
                "%(playlist_index&{} - |)s%(title)s [%(id)s].%(ext)s"
            ),
            url
        ]

    # -----------------------------------------------------
    # GIF
    # -----------------------------------------------------
    elif choice == "5":
        return [
            "yt-dlp",
            "--ignore-errors",
            "--no-overwrites",
            "--continue",
            "--restrict-filenames",
            "-f",
            "bv*[height<=480]/bv*",
            "--recode-video",
            "gif",
            "-o",
            os.path.join(
                DOWNLOAD_DIR,
                "%(playlist_index&{} - |)s%(title)s [%(id)s].%(ext)s"
            ),
            url
        ]


def format_name(choice):
    return {
        "1": "MP3",
        "2": "MP4",
        "3": "AVI",
        "4": "OGG",
        "5": "GIF"
    }[choice]


def download(url, choice):

    command = build_command(url, choice)

    print()
    print(f"{CYAN}Format : {format_name(choice)}{RESET}")
    print(f"{CYAN}Destination : {DOWNLOAD_DIR}{RESET}")
    print()
    print(f"{YELLOW}Téléchargement en cours...{RESET}")
    print()

    try:
        result = subprocess.run(command)

        print()

        if result.returncode == 0:
            print(f"{GREEN}{BOLD}Téléchargement terminé !{RESET}")
            print()
            print(f"Fichiers sauvegardés dans :")
            print(f"{CYAN}{DOWNLOAD_DIR}{RESET}")
        else:
            print(f"{RED}Le téléchargement s'est terminé avec des erreurs.{RESET}")

    except KeyboardInterrupt:
        print()
        print(f"{YELLOW}Téléchargement interrompu.{RESET}")

    except Exception as e:
        print()
        print(f"{RED}Erreur :{RESET}")
        print(e)


def main():

    clear()
    banner()

    check_dependencies()
    create_download_directory()

    while True:

        url = get_url()

        choice = choose_format()

        print()
        print(f"{BOLD}Résumé :{RESET}")
        print(f"URL    : {url}")
        print(f"Format : {format_name(choice)}")
        print(f"Dossier: {DOWNLOAD_DIR}")
        print()

        confirm = input("Commencer le téléchargement ? [O/n] ").strip().lower()

        if confirm in ("", "o", "oui", "y", "yes"):

            download(url, choice)

        else:
            print(f"{YELLOW}Téléchargement annulé.{RESET}")

        print()
        again = input("Télécharger autre chose ? [O/n] ").strip().lower()

        if again not in ("", "o", "oui", "y", "yes"):
            break

        clear()
        banner()

    print()
    print(f"{GREEN}Merci d'avoir utilisé YouTube Downloader !{RESET}")
    print()


if __name__ == "__main__":
    main()
