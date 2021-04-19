#! /usr/local/bin/python3

import os
import sys
from io import BytesIO, StringIO
from unittest.mock import patch
from unittest import TestCase, main
import json
from bedrock_cgi.service_base import ServiceBase, REQUEST_METHOD, REQUEST_METHOD_POST, REQUEST_METHOD_OPTIONS
from bedrock_cgi.cgi_request import CONTENT_LENGTH, CONTENT_TYPE
from bedrock_cgi.cgi_response import HEADER_CONTENT_TYPE
from bedrock_cgi.constant import true, false, MIME_TYPE_JSON, CHARSET, CHARSET_UTF8

def handleOk (event):
    event.ok ({ "OK": "OK" })

class Test (TestCase):
    def testBedrockCgi (self):
        requestString = json.dumps({ "event": "ok" }, ensure_ascii=false).encode(CHARSET_UTF8)
        os.environ[REQUEST_METHOD] = REQUEST_METHOD_POST
        os.environ[CONTENT_TYPE] = "{}; {}={}".format (MIME_TYPE_JSON, CHARSET, CHARSET_UTF8)
        os.environ[CONTENT_LENGTH] = "{}".format (len (requestString))
        with patch ("sys.stdin", new = BytesIO (requestString)), patch("sys.stdout", new=StringIO()) as stdOut:
            ServiceBase.respond ()
            # need to read off the header lines first...
            response = json.loads (stdOut.getvalue().decode(CHARSET_UTF8))
            #self.assertEqual()
            #self.assertEqual(stdOut.getvalue().strip(), expected_out)

if __name__ == '__main__':
    main()

#from bedrock_cgi.service_base import ServiceBase

#ServiceBase.respond()

