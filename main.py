from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Rendering2D import *
from Vector3n import *

mvect = Vector3n(1, 2,3)


width = 1000
height = 750

FPS = 60.0

def update(value):
	global FPS
	glutPostRedisplay()
	glutTimerFunc(int(1000/FPS), update, int(0))

def showScreen():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	iterate()

	fill("FF0000") #hex color with no hashtag
	lWidth(5.0)
	ellipse_arc(400, 400, 100, 50, 0, 360)

	fill("0000FF")
	ellipse(400, 400, 100, 50)


	glutSwapBuffers()

def iterate():
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
	glutInitWindowSize(width, height)
	glutInitWindowPosition(0, 0)
	wind = glutCreateWindow("2D Rendering Engine | Ryan's OpenGL Practice")
	glutDisplayFunc(showScreen)
	#glutIdleFunc(showScreen)
	glutTimerFunc(int(0), update, int(0))
	glutMainLoop()


main()


