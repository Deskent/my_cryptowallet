import os.path

import pytest

from crypto_wallet import CryptoWallet


@pytest.fixture(scope='session')
def wallet_test_name() -> str:
    return "wallet_for_testing"


@pytest.fixture(scope='session')
def wallet_for_test(wallet_test_name, load_passphrase) -> 'CryptoWallet':
    return CryptoWallet(wallet_name=wallet_test_name, passphrase=load_passphrase)


@pytest.fixture(scope='session')
def main_wallet() -> str:
    return "M9SsSjEnBnZCyFKCvXfd1U9VDpjvBKkzfZ"


@pytest.fixture(scope='session')
def load_passphrase(wallet_test_name):
    file_name: str = f"{wallet_test_name}.txt"
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write('')
    with open(file_name) as f:
        passphrase = f.read()
    return passphrase
