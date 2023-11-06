import uuid


def get_mac_address():
    try:
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        formatted_mac = ":".join([mac[i : i + 2] for i in range(0, 12, 2)])
        return formatted_mac
    except Exception as e:
        print("Failed to retrieve MAC address:", str(e))
        return None


# mac_address = get_mac_address()
