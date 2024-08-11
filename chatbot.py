import cleverbotfreeapi

# Without context or session
response = cleverbotfreeapi.cleverbot("Hello.")
print("Without context or session:", response)

# With context, without session
context = ["hi.", "How are you?"]
response = cleverbotfreeapi.cleverbot("Bad.", context)
print("With context, without session:", response)

# Without context, with session
session = "Deftera"
response = cleverbotfreeapi.cleverbot("Hi.", session=session)
print("Without context, with session:", response)
response = cleverbotfreeapi.cleverbot("Fine :)", session=session)
print("Without context, with session:", response)

# With context and session
context = ["hi.", "How are you?"]
session = "How are you?"
response = cleverbotfreeapi.cleverbot("Hello!", context, session)
print("With context and session:", response)

while True:
    user_input = input(">> ")
    response = cleverbotfreeapi.cleverbot(user_input, context, session)
    print(response)
