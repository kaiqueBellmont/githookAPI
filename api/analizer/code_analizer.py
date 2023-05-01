import flake8.main.cli
import sys
import tempfile
from dataclasses import dataclass

@dataclass
class AnalizeCode:
    """
    AnalizeCode class
    """

    @staticmethod
    def analyze(code):
        """
        Analyzes a code and returns errors based on flake8 and PEP8
        """
        error_dict = {}  # Create an empty dictionary to store errors

        for item in code['code_list']:
            for filename, content in item.items():
                print(f"File: {filename}")

                # Create a temporary directory
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_file = tempfile.NamedTemporaryFile(dir=temp_dir, delete=False)
                    temp_filename = temp_file.name

                    # Write the content to the temporary file
                    with open(temp_filename, 'w') as file:
                        file.write(content)

                    error_file = f"{temp_filename}_errors.txt"
                    with open(error_file, 'w') as error_output:
                        sys.stdout = error_output
                        try:
                            flake8.main.cli.main(['--format=pylint', temp_filename])
                        except SystemExit:
                            pass
                        finally:
                            sys.stdout = sys.__stdout__  # Restore standard output

                    # Read the contents of the error file and add to error_dict
                    with open(error_file, 'r') as error_file:
                        error_lines = [line.strip() for line in error_file.readlines() if line.strip()]
                        errors = {}
                        for error_line in error_lines:
                            line_parts = error_line.split(':', 2)
                            if len(line_parts) >= 3:
                                line_number = int(line_parts[1].strip())
                                error_message = line_parts[2].strip()
                                if line_number in errors:
                                    errors[line_number].append(error_message)
                                else:
                                    errors[line_number] = [error_message]
                        error_dict[filename] = errors

        return error_dict
