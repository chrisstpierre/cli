# -*- coding: utf-8 -*-

import click

from .. import cli


@cli.cli.command()
def login():
    # TODO: Add help text
    cli.user()
    click.echo(
        'You\'re logged in as ' +
        click.style(cli.data['email'], fg='cyan')
    )
