import os
import capnp

import preference_capnp


def writeAddressBook(file):
    preference = preference_capnp.Preference.new_message()
    preference.name = "demodemo"
    preference.write(file)


def printAddressBook(file):
    preference = preference_capnp.Preference.read(file)
    print(preference)
    print(preference.name)


if __name__ == '__main__':
    f = open('example', 'w')
    writeAddressBook(f)

    f = open('example', 'r')
    printAddressBook(f)
