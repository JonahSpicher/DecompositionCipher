# DecompositionCipher


In theory we will write two ciphers here:

First, a histogram cipher, it will scramble the letters in a message and make multiple of them based on what order they go in. ...maybe. It sounds hard.

Also though we will make a cipher which encodes a message as a matrix, probably after scrambling it, then encoding the USV matrices and the width in a long string of letters. Just leaving notes here for now, width will be written on the beginning as a two digit number, k will be encoded by number of capitals, and each letter will correspond to a number. A message should look kinda like this:

bdhwk dwnief efniofek Dniwaklsdj

With one capital, the k value would be one, so, the first two letters shifted down one read ac which converts to 13, so the width is thirteen, and you can do math from there.

