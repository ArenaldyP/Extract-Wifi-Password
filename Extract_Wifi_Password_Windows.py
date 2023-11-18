import subprocess
import re
from collections import namedtuple

def get_windows_saved_ssids():
    """Mengembalikan daftar SSID yang disimpan di mesin Windows menggunakan perintah netsh"""
    output = subprocess.check_output("netsh wlan show profiles").decode()
    ssids = [profile.strip().strip(":").strip() for profile in re.findall(r"All User Profile\s(.*)", output)]
    return ssids

def get_windows_saved_wifi_passwords(verbose=1):
    """Mengekstrak kata sandi Wi-Fi yang disimpan di mesin Windows, fungsi ini mengekstrak data menggunakan perintah netsh
    di Windows.

    Args:
        verbose (int, opsional): Apakah ingin mencetak profil yang disimpan secara real-time. Default 1.

    Returns:
        list: Daftar profil yang diekstrak, setiap profil memiliki field ['ssid', 'ciphers', 'key'].
    """
    try:
        ssids = get_windows_saved_ssids()
        Profile = namedtuple("Profile", ["ssid", "ciphers", "key"])
        profiles = []

        for ssid in ssids:
            ssid_details = subprocess.check_output(f"netsh wlan show profile {ssid} key=clear").decode()
            ciphers = "/".join([c.strip().strip(":").strip() for c in re.findall(r"Cipher\s(.*)", ssid_details)])

            # Dapatkan Kata Sandi Wi-Fi
            key = re.findall(r"Key Content\s(.*)", ssid_details)
            key = key[0].strip().strip(":").strip() if key else "None"

            profile = Profile(ssid=ssid, ciphers=ciphers, key=key)

            if verbose >= 1:
                print_windows_profile(profile)

            profiles.append(profile)

        return profiles
    except subprocess.CalledProcessError as e:
        print(f"Terjadi kesalahan saat menjalankan perintah netsh: {e}")
        return []

def print_windows_profile(profile):
    """Mencetak satu profil pada Windows"""
    print(f"{profile.ssid:25} {profile.ciphers:15} {profile.key:50}")

def print_windows_profiles(verbose):
    """Mencetak semua SSID yang diekstrak beserta kata sandinya di Windows"""
    print("SSID         CIPHERS(S)          KEY")
    print("-" * 50)
    get_windows_saved_wifi_passwords(verbose)


if __name__ == "__main__":
    get_windows_saved_wifi_passwords()
