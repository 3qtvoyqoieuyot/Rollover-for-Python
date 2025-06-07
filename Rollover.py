def runprogram(prg):
    cells = [0]
    maxlength = 255
    maxvalue = 255
    currcellnum = 0
    currChar = ""
    loopid = 0
    loopstart = 0
    output = ""

    i = 0
    while i < len(prg):
        currChar = prg[i]
        if currChar == "n":
            currcellnum += 1
            if currcellnum >= len(cells):
                cells.append(0)
            if currcellnum > maxlength:
                currcellnum = 0
        elif currChar == "i":
            cells[currcellnum] += 1
            if cells[currcellnum] > maxvalue:
                cells[currcellnum] = 0
        elif currChar == "c":
            if i + 1 < len(prg) and prg[i + 1] == "[":
                loopid += 1
                loopstart = i + 2
                startingcell = currcellnum

                loopBody = ""
                bracketDepth = 1
                j = i + 2
                while j < len(prg):
                    if prg[j] == "[":
                        bracketDepth += 1
                    elif prg[j] == "]":
                        bracketDepth -= 1
                    if bracketDepth == 0:
                        break
                    loopBody += prg[j]
                    j += 1
                i = j

                while cells[currcellnum] != currcellnum:
                    runprogram(loopBody)
            else:
                print("Rollover: Loop Start Error at character {i}; The loop does not have the starting bracket '[]' and instead has '{prg[i + 1]}'.")
        elif currChar == "[":
            if i == 0 or prg[i - 1] != "c":
                print("Rollover: Loop Reference Error at character {i}; A loop is started without the loop command and instead uses '{prg[i - 1]}'.")
        elif currChar == "p":
            output += str(cells[currcellnum])
        elif currChar == "u":
            output += chr(cells[currcellnum])
        elif currChar == "a":
            if cells[currcellnum] < 128:
                output += chr(cells[currcellnum])
            else:
                print("Rollover: ASCII Print Error at character {i}; The requested character of value '{cells[currcellnum]}' is not ASCII.")
        else:
            print("Rollover: Input Error at character {i}; An unknown character was used in the program: '{prg[i]}'.")
        i += 1

    print(output)
    print(cells)
print("Rollver Compiler for Python, made by 31parkjulian")
runprogram(input("Enter Rollover Code:"))
