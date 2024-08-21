"""Comandos Cli

El banner para la consola se realizó usando esta herramienta WEB
https://fsymbols.com/generators/tarty/
Esta web creó un texto gigante que fue modificado para hacerlo mas minimalista.
"""

import click

from .app_info import AppInfo

@click.group()
def cli():
    """
    
    ███╗░░██╗███████╗░██╗░░░░░░░██╗░██████╗
    ████╗░██║██╔════╝░██║░░██╗░░██║██╔════╝
    ██╔██╗██║█████╗░░░╚██╗████╗██╔╝╚█████╗░
    ██║╚████║██╔══╝░░░░████╔═████║░░╚═══██╗
    ██║░╚███║███████╗░░╚██╔╝░╚██╔╝░██████╔╝
    ╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░╚═════╝░

    ░█████╗░███╗░░██╗░█████╗░██╗░░░░░██╗░░░██╗░██████╗██╗░██████╗
    ██╔══██╗████╗░██║██╔══██╗██║░░░░░╚██╗░██╔╝██╔════╝██║██╔════╝
    ███████║██╔██╗██║███████║██║░░░░░░╚████╔╝░╚█████╗░██║╚█████╗░
    ██╔══██║██║╚████║██╔══██║██║░░░░░░░╚██╔╝░░░╚═══██╗██║░╚═══██╗
    ██║░░██║██║░╚███║██║░░██║███████╗░░░██║░░░██████╔╝██║██████╔╝
    ╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═════╝░╚═╝╚═════╝░
    """
    pass

@cli.command()
def version():
    """Muestra la versión de la aplicación"""
    click.echo(AppInfo().version)

@cli.command()
def app_info():
    """Devuelve información de la aplicación"""
    click.echo(AppInfo().to_dict())

if __name__ == '__main__':
    cli()