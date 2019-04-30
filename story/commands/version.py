# -*- coding: utf-8 -*-

import click

from .. import cli


@cli.cli.command()
def version():
    """Prints the 'story' and Storyscript Compiler versions.
    """
    from storyscript import version

    click.echo(
        click.style('Asyncy', fg='magenta') + ' ' +
        cli.version + click.style(' - ', dim=True) +
        click.style('Storyscript', fg='cyan') + ' ' +
        version
    )
