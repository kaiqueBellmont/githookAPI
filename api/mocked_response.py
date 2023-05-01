worker_response = {
    "str_response": "\n\n1. The indentation should be consistent throughout the code.\n2. For the apagar2.py code, "
                    "the string should be broken up into multiple lines for better readability.\n3. The "
                    "hook/formatter.py code should use lowerCamelCase instead of snake_case for variables.\n4. The "
                    "hook/formatter.py code could have better organization, such as organizing the methods into "
                    "related groups.\n5. The hook/formatter.py code could benefit from using descriptive, "
                    "clear comments to help explain code functionality."
}

analize_response = {
    "apagar2.py": {
        "1": [
            "[F401] 'datetime' imported but unused"
        ],
        "3": [
            "[E302] expected 2 blank lines, found 1"
        ],
        "8": [
            "[E305] expected 2 blank lines after class or function definition, found 1",
            "[E501] line too long (135 > 79 characters)"
        ]
    },
    "hook/formatter.py": {
        "32": [
            "[E501] line too long (94 > 79 characters)"
        ]
    }
}