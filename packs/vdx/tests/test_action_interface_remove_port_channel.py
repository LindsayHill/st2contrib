"""Generated test for checking pynos based actions
"""
import xml.etree.ElementTree as ET
from st2tests.base import BaseActionTestCase
from interface_remove_port_channel import interface_remove_port_channel

__all__ = [
    'TestInterfaceRemovePortChannel'
]


class MockCallback(object):  # pylint:disable=too-few-public-methods
    """Class to hold mock callback and result
    """
    returned_data = None

    def callback(self, call, **kwargs):  # pylint:disable=unused-argument
        """Mock callback method
        """
        xml_result = ET.tostring(call)
        self.returned_data = xml_result


class TestInterfaceRemovePortChannel(BaseActionTestCase):
    """Test holder class
    """
    action_cls = interface_remove_port_channel

    def test_action(self):
        """Generated test to check action
        """
        action = self.get_action_instance()
        mock_callback = MockCallback()
        kwargs = {
            'username': '',
            'ip': '',
            'password': '',
            'port': '22',
            'port_int': '3',
            'test': True,
            'callback': mock_callback.callback
        }

        action.run(**kwargs)

        expected_xml = (
            '<config><interface xmlns="urn:brocade.com:mgmt:brocade-interface"'
            '><port-channel operation="delete"><name>3</name></port-channel></'
            'interface></config>'
        )

        self.assertTrue(expected_xml, mock_callback.returned_data)
