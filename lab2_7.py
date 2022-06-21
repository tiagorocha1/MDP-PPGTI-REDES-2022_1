from ncclient import manager

def exec():
    m = manager.connect(
        host="192.168.18.47",
        port=830,
        username="cisco",
        password="cisco123!",
        hostkey_verify=False
    )

    print("#Supported Capabilities (YANG models):")
    for capability in m.server_capabilities:
        print(capability)

if __name__ == '__main__':
    exec()