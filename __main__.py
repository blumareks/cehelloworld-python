# use third-party 'lorem-ipsum' package to generate random words
from lorem_text import lorem
# 

# Create a requirements.txt containing your required dependencies for your function
# for example place `lorem-text` in the file (no quotes)

# The `main` function is the entry-point into the function.
# It has one optional argument, which carries all the 
# parameters the function was invoked with.
def main(params):
    words = 10

    # since functions are invoked through http(s), we return an HTTP response
    return {
      "headers": {
        "Content-Type": "text/plain;charset=utf-8",
    },
    "body": lorem.words(words),
##    "body": "Hello World!"
}