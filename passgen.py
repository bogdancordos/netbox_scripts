import string
from random import *
from extras.scripts import *


class PassGen(Script):
    class Meta:
        name = "Password Generator"
        description = "Generate 5 passwords, 16 characters long "

    def run(self, data, commit):
        characters = string.ascii_letters + string.digits
        password01 =  "".join(choice(characters) for x in range(randint(16, 16)))
        password02 =  "".join(choice(characters) for x in range(randint(16, 16)))
        password03 =  "".join(choice(characters) for x in range(randint(16, 16)))
        password04 =  "".join(choice(characters) for x in range(randint(16, 16)))
        password05 =  "".join(choice(characters) for x in range(randint(16, 16)))

        passwords = [password01, password02, password03, password04, password05]
        output=('\n'.join(map(str, passwords)))
        self.log_success(f"Password one:   {password01}")
        self.log_success(f"Password two:   {password02}")
        self.log_success(f"Password three: {password03}")
        self.log_success(f"Password four:  {password04}")
        self.log_success(f"Password five:  {password05}")
        return ('\n'.join(map(str, passwords)))
