#!/usr/bin/python

# base64 cipher [encoding] package for the the codex project
# created by : C0SM0

# imports
import base64
import getopt
import sys

# help menu for cipheringing process
help_menu = """
        [+] ARGUMENTS Base64
        [+] ARG 1. Process
                [-e] ---------- Encrypt
                [-d] ---------- Decrypt

        [+] ARG 2. Additional Aruments
                [-t <plaintext>] --------- Input Text
                [-i <input file>] -------- Input File [.txt]
                [-o <output file>] ------- Output File

        [+] Example:
        cryptex -b64 -e -t hello
        """

# encode base64
def encode_base64(plain_content, print_cnt):

    encoded_cnt = plain_content.encode('ascii')
    b64_bytes = base64.b64encode(encoded_cnt)
    output = b64_bytes.decode('ascii')

    # output content to cli
    if print_cnt == True:
        print(f'Encrypted Content:\n{output}\n')

    # output content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(output)
        print('Output written to file sucessfully')

# encode base64
def decode_base64(plain_content, print_cnt):

    decoded_cnt = plain_content.encode('ascii')
    b64_bytes = base64.b64decode(decoded_cnt)
    output = b64_bytes.decode('ascii')

    # output content to cli
    if print_cnt == True:
        print(f'Encrypted Content:\n{output}\n')

    # output content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(output)
        print('Output written to file sucessfully')

# parse all arguments
def b64_parser():
    opts, args = getopt.getopt(sys.argv[2:], 'i:t:o:', ['inputFile', 'inputText', 'outputFile'])
    arg_dict = {}

    # loop through arguments, assign them to dict [arg_dict]
    for opt, arg in opts:
        # input options
        if opt == '-i':
            arg_dict['-i'] = arg
        if opt == '-t':
            arg_dict['-t'] = arg
        # output options
        if opt == '-o':
            arg_dict['-o'] = arg

    return arg_dict

# command line interface
def cli(argument_check):

    # one liners
    if argument_check == True:

        # tries to get all arguments
        try:
            arguments = b64_parser()

        # catches arguments with no value
        except getopt.GetoptError:
            print(f'[!!] No value was given to your argument\n{help_menu}')

        # continues with recieved arguments
        else:    
            # getting variables for ciphering process
            inputted_content = arguments.get('-t')
            print_content = True
            
            # checks users output type
            if ('-i' in arguments):
                # tries to read file
                try:
                    inputted_content = open(arguments.get('-i'), 'r').read()
                    inputted_content = inputted_content[2::2]

                # file does not exist
                except FileNotFoundError:
                    print('[!!] he attached file does not exist')

            # checks if output was specified
            if ('-o' in arguments):
                print_content = arguments.get('-o')

            ciphering_process = sys.argv[1]

            # attempts to run cipher
            try:
                # encodes base64
                if ciphering_process == '-e':
                    encode_base64(inputted_content, print_content)

                # decodes base64
                if ciphering_process == '-d':
                    decode_base64(inputted_content, print_content)

            # catches unspecified arguments
            except TypeError:
                print(f'[!!] No Key or Argument was specified\n{help_menu}')

    # help menu 
    else:
        print(help_menu)

# main code
def b64_main():

    # checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True

    cli(arguments_exist)

# runs main function if file is not being imported
if __name__ == '__main__':
    b64_main()