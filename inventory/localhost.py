#!/usr/bin/env python3

import json
import socket


hostname = socket.gethostname()

print(
    json.dumps(
        {
            "_meta": {
                "hostvars": {
                    hostname: {
                        "ansible_connection": "local",
                        "ansible_python_interpreter": "/usr/bin/python3",
                    }
                }
            },
            "all": {"hosts": [hostname]},
        }
    )
)
