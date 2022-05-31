from src.crypto_wallet.crypto_wallet import CryptoWallet, wallet_delete


async def test_get_address_for_new_user():
    telegram_id: str = str('1234567890')  # Получить телеграм ИД пользователя из БД
    wallet_name: str = f"w_{telegram_id}"
    try:
        wallet_delete(wallet_name)
    except Exception:
        pass
    wallet: 'CryptoWallet' = await CryptoWallet(wallet_name=wallet_name, owner=telegram_id).get_wallet()
    passphrase = wallet.passphrase
    wallet_data = await CryptoWallet(wallet_name=wallet_name, owner=telegram_id, passphrase=passphrase).info()
    assert wallet_data
"""
wallet_data: dict = {
    "wallet_id": 23,
    "name": "wallet_for_vasya",
    "owner": "vasya",
    "address": "LZT5ZB1XB9X9E8qdnx4L2Qk5SEpNRjYPNS",
    "main_network": "litecoin",
    "main_balance": 0.0,
    "main_balance_str": "0.00000000 LTC"
}
"""
