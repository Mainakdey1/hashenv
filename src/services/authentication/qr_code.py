import qrcode
import json
import uuid
from pathlib import Path
from platformdirs import user_config_dir

CONFIG_DIR = Path(user_config_dir("hashenv", appauthor=False))
DEVICE_FILE = CONFIG_DIR / "device.json"



def display_qr_code(device_token_id : str) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=1,
        border=2
    )
    qr.add_data(device_token_id)
    qr.make(fit=True)

    qr.print_ascii(invert=True)





def get_device_id() -> str:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    if DEVICE_FILE.exists():
        data = json.loads(DEVICE_FILE.read_text(encoding="utf-8"))
        device_id = data.get("device_token_id")

        if device_id:
            return device_id

    device_id = str(uuid.uuid4())

    DEVICE_FILE.write_text(
        json.dumps({"device_token_id": device_id}, indent=2),
        encoding="utf-8",
    )

    return device_id
