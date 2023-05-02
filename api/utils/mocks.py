code_list = {
    "code_list": [
        {
            "hook/formatter.py": 'from dataclasses import dataclass\n\n\n@dataclass\nclass Formatter:\n    """\n    Formatter class\n    """\n\n    @staticmethod\n    def show_request_result(result):\n        """\n        :param result: Result from request\n        """\n        for file, erros in result.items():\n            print(f"Result for File: {file}:")\n            for line, messages in erros.items():\n                formatted_messages = "\\n\\t".join(messages)\n                print(f"Line {line}:\\n\\t{formatted_messages}")\n\n    @staticmethod\n    def show_in_code_format(codes):\n        """\n        print in python code format\n        :param: code\n            data = {\n                \\\'code_list\\\': code_list\n            }\n            # Example codes\n            codes = {\n                \\\'code_list\\\': [\n                    {\\\'exampl.py\\\': \\\'import datetime\\n\\ndef soma(a, b):\\n    return a + b\\\'},\n                    ]\n            }\n        """\n        for code in codes["code_list"]:\n            for filename, content in code.items():\n                print(f"File: {filename}")\n                print(content)\n'
        }
    ]
}
