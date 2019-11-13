import json
import logging
import chardet
import os
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.snapshot import pgi_name
from ruxit.api.data import PluginStateMetric


class EncodingCheckPlugin(BasePlugin):

    def check_encoding(self, path, desired_encoding, file_extension):
        #list all files in directory 
        from os import walk

        filenames = []
        for (dirpath, dirnames, filenames) in walk(path):
            filenames.extend(filenames)
            break
        files_to_check = [fname for fname in filenames if (file_extension in fname)] 

        #check all files found with that file extension in directory
        for filename in files_to_check:
            with open((path + "\\" + filename ), "rb") as f:
                result = chardet.detect(f.read())["encoding"]
                if result != desired_encoding:
                    return "incorrect_encoding", filename
        return "correct_encoding", None
            

    def query(self, **kwargs):
        config = kwargs["config"]
        filepath = config["filepath"]
        desired_encoding = config["encoding_type"]
        file_extension = config["file_extension"]
        if file_extension[0:1] != ".":
            file_extension = "." + file_extension
        # pgi = self.find_single_process_group(pgi_name('plugin_sdk.demo_app'))
        # pgi_id = pgi.group_instance_id#
        
        matches_encoding, failed_file = self.check_encoding(filepath, desired_encoding, file_extension)
        #return results
        self.results_builder.add_absolute_result(
            PluginStateMetric(key="matches_encoding", value=matches_encoding)
        )
        if failed_file:
            self.results_builder.report_error_event(description = "Encoding not Matched", title = "Encoding Not Matched", properties = {"filename":failed_file})



