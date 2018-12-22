# -*- coding: utf-8 -*-
import json
import os

import click

import click_spinner

from storyscript.App import App

from .. import cli, options
from ..api import Config, Releases


@cli.cli.command(aliases=['deploy'])
@click.option('--message', is_flag=True, help='Deployment message')
@options.app
def deploy(app, message):
    cli.user()
    cli.assert_project(app)
    click.echo(f'Deploying app {app}... ', nl=False)
    with click_spinner.spinner():
        config = Config.get(app)
        payload = json.loads(App.compile(os.getcwd()))
        release = Releases.create(config, payload, app, message)
    url = f'https://{app}.asyncyapp.com'
    click.echo()
    click.echo(click.style('√', fg='green') +
               f' Version {release["id"]} of your app has '
               f'been queued for deployment.\n\n'
               f'Check the deployment status with:')
    cli.print_command('asyncy releases')
    click.echo()
    click.echo(f'If your story listens to HTTP requests, visit {url}')
