# -*- coding: utf-8 -*-
from datetime import datetime

import click

import click_spinner

import requests

from .. import cli
from .. import options
from ..api import Apps


@cli.cli.command()
@click.option('--follow', '-f', is_flag=True, help='Follow the logs')
@options.app()
def logs(follow, app):
    """
    Show application logs
    """
    if follow:
        click.echo('-f (following log output) is not supported yet.')
        return

    cli.user()

    url = 'https://stories.asyncyapp.com/logs'
    click.echo(f'Retrieving logs for {app}... ', nl=False)
    with click_spinner.spinner():
        app_id = Apps.get_uuid_from_hostname(app)
        r = requests.get(url, params={
            'app_id': app_id,
            'access_token': cli.get_access_token()
        })

    click.echo()

    try:
        arr = r.json()
        assert isinstance(arr, list)
    except BaseException:
        click.echo('Logs for your app aren\'t available right now.\n'
                   'If this error persists, please shoot us an email '
                   'on support@asyncy.com', err=True)
        import sys
        sys.exit(1)

    cli.track('App Logs Retrieved', {'App name': app, 'Log count': len(arr)})

    if len(arr) == 0:
        click.echo(f'No logs found for {app}')
        return

    arr.reverse()  # Latest is at the head.

    for log in arr:
        message = log['payload']['message']
        level = log['payload']['level'][:6].rjust(6)

        # Replace the ":" in the timezone field for datetime.
        ts = log['timestamp']
        ts = ts[0:ts.rindex(':')] + ts[ts.rindex(':') + 1:]
        date = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S.%f%z')

        pretty_date = date.astimezone().strftime('%b %d %H:%M:%S')
        colourize_and_print(pretty_date, level, message)


def colourize_and_print(date, level, message):
    level_col = 'green'  # Default for info.
    level = level.lower()
    if 'debug' in level:
        level_col = 'blue'
    elif 'warn' in level:
        level_col = 'yellow'
    elif 'crit' in level or 'error' in level:
        level_col = 'red'

    click.echo(f'{click.style(date, fg="white")} '
               f'{click.style(level.upper(), fg=level_col)} '
               f'{message}')
