import turtle
import math

#GLOBALS
g_gridX=800
g_gridY=800

def changeBounds():
	while True:
		try:
			lx = int(input("Enter a lower x bound"))
		except:
			print("enter a number")
			continue

		try:
			ux = int(input("Enter an upper x bound"))
		except:
			print("enter a number")
			continue

		if not lx<ux:
			continue
		break
	xTuple = (lx,ux)

	while True:
		try:
			ly = int(input("Enter a lower y bound"))
		except:
			print("enter a number")
			continue

		try:
			uy = int(input("Enter an upper y bound"))
		except:
			print("enter a number")
			continue

		if not ly<uy:
			continue
		break
	yTuple = (ly,uy)

	return xTuple,yTuple

def drawGrid(xBounds,yBounds):
	turtle.tracer(0)
	turtle.hideturtle()
	turtle.pensize(3)
	turtle.setup(width = g_gridX+50,height=g_gridY+50,startx = None, starty = None)
	print(turtle.pos())
	armlength=[g_gridX,g_gridY,g_gridY,g_gridX]
	armlabel=[xBounds[1],yBounds[1],xBounds[0],yBounds[0]]
	for arm in range(0,4):
		for mark in range(1,11):
			turtle.forward(armlength[arm]/20)
			turtle.right(90)
			turtle.forward(5)
			turtle.backward(5)
			turtle.left(90)
		turtle.penup()
		turtle.right(90)
		turtle.forward(20)
		turtle.write(armlabel[arm])
		turtle.backward(20)
		turtle.left(90)
		turtle.pendown()
		turtle.backward(armlength[arm]/2)
		turtle.left(90)
	turtle.pensize(1)
	turtle.update()


def parse(inpStr):
	newStr = inpStr
	newStr = newStr.replace("x","float({})")
	newStr = newStr.replace("pow","math.pow")
	newStr = newStr.replace("sin","math.sin")
	newStr = newStr.replace("cos","math.cos")
	print(newStr)
	return newStr

def plot(function,xBounds,yBounds):
	print("hello")
	turtle.pensize(2)
	turtle.left(180)
	turtle.forward(g_gridX/2)
	increment = (xBounds[1]-xBounds[0])/g_gridX
	turtle.penup()
	try:
		y=eval(function.format(xBounds[0]))
		#print(((y-yBounds[0])*g_gridY)/(yBounds[1]-yBounds[0])-g_gridY/2)
		turtle.goto(turtle.pos()[0],((y-yBounds[0])*g_gridY)/(yBounds[1]-yBounds[0])-g_gridY/2)
	except:
		pass
	turtle.color("red")
	
	for i in range(0,g_gridX+1):

		turtle.pendown()
		try:
			y=eval(function.format(xBounds[0]+increment*i))
			if y>yBounds[1] or y<yBounds[0]:
				turtle.penup()
			print(((y-yBounds[0])*g_gridY)/(yBounds[1]-yBounds[0])-g_gridY/2)
			turtle.goto(turtle.pos()[0]+1,((y-yBounds[0])*g_gridY)/(yBounds[1]-yBounds[0])-g_gridY/2)
		except:
			turtle.penup()

		


if __name__ == "__main__":

	while True:
		print("type 'help' for list of supported functions and 'exit' to leave")
		print("Enter function:")
		userInput = input("f(x)=")

		if userInput == "help":
			listFunctions()
			continue

		if userInput == "exit":
			exit()

		parsedFunc = parse(userInput)
		if parsedFunc == "invalid":
			continue

		print("default bounds \nx:-10 -> 10\ny:-10 -> 10")
		xBound = (-10,10)
		yBound = (-10,10)
		if not input("type anything to change bounds or enter to keep default")=="":
			while True:
				result = changeBounds()
				if result == -1:
					continue
				else:
					xBound,yBound = result
					break

		drawGrid(xBound,yBound)
		plot(parsedFunc,xBound,yBound)
		print("Close the graph window to enter a new function")
		turtle.done()
		