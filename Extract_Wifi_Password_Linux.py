import configparser
import os
from collections import namedtuple


def get_linux_saved_wifi_passwords(verbose=1):
    """Mengambil kata sandi Wi-Fi yang disimpan pada mesin Linux dari direktori '/etc/NetworkManager/system-connections/'.

    Args:
        verbose (int, opsional): Menentukan apakah ingin mencetak profil yang disimpan secara real-time. Default 1.

    Returns:
        [list]: Daftar profil yang diekstraksi, setiap profil memiliki field ['ssid', 'auth-alg', 'key-mgmt', 'psk'].
    """
    network_connections_path = "/etc/NetworkManager/system-connections/"
    fields = ["ssid", "auth-alg", "key-mgmt", "psk"]
    Profile = namedtuple("Profile", [f.replace("-", "_") for f in fields])
    profiles = []

    for file in os.listdir(network_connections_path):
        data = {k.replace("-", "_"): None for k in fields}
        config = configparser.ConfigParser()
        config.read(os.path.join(network_connections_path, file))

        for _, section in config.items():
            for k, v in section.items():
                if k in fields:
                    data[k.replace("-", "_")] = v

        profile = Profile(**data)
        if verbose >= 1:
            print_linux_profile(profile)

        profiles.append(profile)

    return profiles


def print_linux_profile(profile):
    """Mencetak satu profil pada sistem Linux."""
    print(f"{str(profile.ssid):25} {str(profile.auth_alg):5} {str(profile.key_mgmt):10} {str(profile.psk):50}")


def print_linux_profiles(verbose):
    """Mencetak semua SSID yang diekstraksi beserta kata sandi (PSK) pada sistem Linux."""
    print("SSID     Auth    Key-MGMT    PSK")
    print("-" * 50)
    get_linux_saved_wifi_passwords(verbose)


def print_profiles(verbose=1):
    """Mencetak profil Wi-Fi yang disimpan berdasarkan sistem operasi.

    Args:
        verbose (int, opsional): Menentukan apakah ingin mencetak profil yang disimpan secara real-time. Default 1.
    """
    if os.name == "posix":
        print_linux_profiles(verbose)
    else:
        raise NotImplementedError("Kode hanya berfungsi untuk Linux")


if __name__ == "__main__":
    print_profiles()
