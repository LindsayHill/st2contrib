from st2actions.runners.pythonrunner import Action
from clicrud.device.generic import generic


class ClicrudRead(Action):

    def run(self, **kwargs):
        commands = kwargs.pop('commands')

        # If port is not specified, ST2 passes it is as None
        # This breaks clicrud, so better to remove it here
        if kwargs.get('port'):
            if kwargs['port'] is None:
                kwargs.pop('port')

        # Same issue with enable
        if kwargs.get('enable'):
            if kwargs['enable'] is None:
                kwargs.pop('enable')

        transport = generic(**kwargs)

        response = transport.read(commands, return_type="string")
        transport.close()
        return response
