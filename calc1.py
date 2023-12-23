INTEGER, PLUS, EOF = "INTEGER", "PLUS", "EOF"

class Token:
	def __init__(self, type, value):
		self.type = type
		self.value = value

	def __str__(self):
		return f"Token({self.type}, {self.value})"

	def __repr__(self):
		return self.__str__()


class Interpreter:
	def __init__(self, text):
		self.text = text
		self.pos = 0
		self.current_token = None

	def error(self):
		raise Exception('Error parsing input')

	def get_next_token(self):
		text = self.text

		if self.pos > len(text) - 1:
			return Token(EOF, None)

		current_char = text[self.pos]

		if current_char.isdigit():
			self.pos += 1
			return Token(INTEGER, int(current_char))

		if current_char == "+":
			self.pos += 1
			return Token(PLUS, current_char)

		return self.error()

	def eat(self, token_type):
		if token_type == self.current_token.type:
			self.current_token = self.get_next_token()
		else:
			self.error()

	def expr(self):
		self.current_token = self.get_next_token()

		value1 = self.current_token.value
		self.eat(INTEGER)
		self.eat(PLUS)
		value2 = self.current_token.value
		self.eat(INTEGER)

		return value1 + value2

if __name__=="__main__":
	while True:
		text = input("calc>")
		interpreter = Interpreter(text)
		print(interpreter.expr())