import json
import os
from tempfile import NamedTemporaryFile

from click.testing import CliRunner, Result

# import delegator

import pytest

STORYSCRIPT_CONFIG = {
    'id': os.environ['STORYSCRIPT_INT_CONF_USER_ID'],
    'access_token': os.environ['STORYSCRIPT_INT_CONF_ACCESS_TOKEN']
}


@pytest.fixture
def runner(magic):
    cli_runner = CliRunner()

    def function(command_function, exit_code, *args) -> Result:
        result = cli_runner.invoke(command_function, args)
        if result.exception is not None \
                and not isinstance(result.exception, SystemExit):
            print(result.exc_info)
            # TODO: find a way to print the exception traceback
            # TODO: it's not straightforward
            assert False

        assert result.exit_code == exit_code
        return result

    out = magic()
    out.run = function
    out.runner = cli_runner
    return out


# @pytest.fixture
# def cli():
#     def function(*args, logged_in=True):
#
#         tf = NamedTemporaryFile().name
#
#         if logged_in:
#             # Create a temporary config file.
#             with open(tf, 'w') as f:
#                 f.write(json.dumps(STORYSCRIPT_CONFIG))
#
#         # Make temporary file.
#         args = ' '.join(args)
#         c = delegator.run(f'story {args}', env={'TOXENV': 'true',
#                                                 'STORY_CONFIG_PATH': tf})
#
#         os.remove(tf)
#         return c
#
#     return function


@pytest.fixture
def magic(mocker):
    """
    Shorthand for mocker.MagicMock. It's magic!
    """
    return mocker.MagicMock


@pytest.fixture
def patch_init(mocker):
    """
    Makes patching a class' constructor slightly easier
    """
    def patch_init(item):
        mocker.patch.object(item, '__init__', return_value=None)
    return patch_init


@pytest.fixture
def patch_many(mocker):
    """
    Makes patching many attributes of the same object simpler
    """
    def patch_many(item, attributes):
        for attribute in attributes:
            mocker.patch.object(item, attribute)
    return patch_many


@pytest.fixture
def patch(mocker, patch_init, patch_many):
    mocker.patch.init = patch_init
    mocker.patch.many = patch_many
    return mocker.patch


@pytest.fixture
def app_dir():
    pass
