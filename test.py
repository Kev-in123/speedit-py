from speedit import speed

@speed
def hi_there():
  print("hi there")

hi_there()

@speed
def hello_there(msg):
  print(msg)

hello_there("hello there")
