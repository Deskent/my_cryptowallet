import os
from decimal import Decimal

import pytest

from crypto_wallet.crypto_wallet import CryptoWallet, WalletError, wallet_delete


async def test_delete_before_testing_error(wallet_test_name):
    with pytest.raises(WalletError):
        wallet_delete(wallet_test_name)


async def test_create_new_wallet_without_name():
    with pytest.raises(TypeError):
        CryptoWallet()


async def test_get_wallet_wrong_passphrase(wallet_test_name):
    passphrase = "random"
    with pytest.raises(ValueError):
        await CryptoWallet(wallet_name=wallet_test_name, passphrase=passphrase).load_data()


async def test_create_new_wallet(wallet_for_test, wallet_test_name):
    wallet: 'CryptoWallet' = await wallet_for_test.get_wallet()
    with open(f"{wallet_test_name}.txt", 'w', encoding='utf-8') as f:
        f.write(wallet.passphrase)
    assert wallet.wallet.name == wallet_test_name


async def test_get_wallet_right_passphrase(wallet_for_test, wallet_test_name):
    wallet: 'CryptoWallet' = await wallet_for_test.load_data()
    assert wallet.wallet.name == wallet_test_name


async def test_send_money_zero_balance_error(wallet_for_test, main_wallet):
    balance_str: str = await wallet_for_test.get_wallet_balance_str()
    assert not await wallet_for_test.send_money(amount=balance_str, address=main_wallet)


async def test_get_wallet_from_passphrase(wallet_for_test, wallet_test_name, load_passphrase):
    wallet: 'CryptoWallet' = await wallet_for_test.get_wallet()
    assert wallet.wallet.name == wallet_test_name


@pytest.mark.parametrize('network, fee', [("litecoin", Decimal(0.0015)),
                                          ('bitcoin', 0)])
async def test_get_fee(network, fee, wallet_for_test):
    wallet_for_test._network = network
    assert wallet_for_test._get_fee() == fee


async def test_get_wallet_balance(wallet_for_test):
    balance: 'Decimal' = await wallet_for_test.get_wallet_balance()
    assert isinstance(balance, Decimal)


async def test_get_wallet_balance_with_fee(wallet_for_test):
    balance: str = await wallet_for_test.get_wallet_balance_str()
    assert isinstance(balance, str)


async def test_get_wallet_address(wallet_for_test):
    address: str = await wallet_for_test.get_wallet_address()
    assert isinstance(address, str)


async def test_delete_wallet(wallet_for_test):
    await wallet_for_test.load_data()
    assert await wallet_for_test.delete_wallet() is True


async def test_delete_wallet_not_exists(wallet_for_test):
    assert await wallet_for_test.delete_wallet() is False


def test_delete_file(wallet_test_name):
    assert os.system(f"rm {wallet_test_name}.txt") == 0
