import string
from random import *
from extras.scripts import *


class PassGen(Script):
    class Meta:
        name = "Password Generator"
        description = "Generate n passwords, y characters long "

    def run(self, data, commit):
        characters = string.ascii_letters + string.digits
        password01 =  "".join(choice(characters) for x in range(randint(y, y)))


        passwords = [password01]
        output=('\n'.join(map(str, passwords)))
        self.log_success(f"Password one:   {password01}")

        return ('\n'.join(map(str, passwords)))
