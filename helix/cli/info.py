#! /usr/bin/env python3
import click
from helix.config import Config 
from helix.services.wallet import Wallet 
from helix.print import Print
from helix.constants import PrintType

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def get_address():
    """get address"""
    config = Config()
    wallet = Wallet(config.get_keypair_path())

    if not wallet.is_wallet_exited():
        Print(PrintType.ERROR)._out("Wallet not found, please create wallet first")
        print("")

        quit()

    address = wallet.get_address()

    # Print.print_success(address)
    Print()._out(message=address)
    print("")

@click.group()
def info_command():
    """Get info of wallet"""
    pass

info_command.add_command(get_address, "address")