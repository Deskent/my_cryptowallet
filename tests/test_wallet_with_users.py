from crypto_wallet.wallet import CryptoWallet, wallet_delete


async def test_get_address_for_new_user():
    telegram_id: str = str('1234567890')
    wallet_name: str = f"w_{telegram_id}"
    try:
        wallet_delete(wallet_name)
    except Exception:
        pass
    wallet: 'CryptoWallet' = await CryptoWallet(wallet_name=wallet_name).get_wallet()
    assert await CryptoWallet(wallet_name=wallet_name, passphrase=wallet.passphrase).info()
