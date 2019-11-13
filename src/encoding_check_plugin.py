import json
import logging
import chardet
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.snapshot import pgi_name
from ruxit.api.data import PluginStateMetric


class EncodingCheckPlugin(BasePlugin):

    def check_encoding(self, filename, desired_encoding):
        with open(filename, "rb") as f:
            result = chardet.detect(f.read())["encoding"]
        if result == desired_encoding:
            return "correct_encoding"
        else: 
            return "incorrect_encoding"

    def query(self, **kwargs):
        config = kwargs["config"]
        filepath = config["filepath"]
        desired_encoding = config["encoding_type"]
        # pgi = self.find_single_process_group(pgi_name('plugin_sdk.demo_app'))
        # pgi_id = pgi.group_instance_id#

        #return results
        self.results_builder.add_absolute_result(
            PluginStateMetric(key="matches_encoding", value=self.check_encoding(filepath, desired_encoding))
        )



