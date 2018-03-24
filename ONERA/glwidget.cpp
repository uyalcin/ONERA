#include "glwidget.h"

float rand_a_b(int a, int b)
{
    return (rand()%(b-a)+a) / 100.0f;
}

GLWidget::GLWidget(QWidget *parent):
    QGLWidget(parent),
    state(0)
{
    Vector3 pos(0, 0, 0);
    Box b(Vector3(2, 2, 2));
    b.setPosition(pos);
    boxs.push_back(b);

    // Random colors
    for(int i = 0; i < nbBoxs(); i++)
    {
        color c;
        c.r = rand_a_b(0, 100);
        c.g = rand_a_b(0, 100);
        c.b = rand_a_b(0, 100);
        c.a = 0.5;
        colors.push_back(c);
    }
}

void GLWidget::initializeGL()
{
    glClearColor(0.2, 0.2, 0.2, 1);
}

void GLWidget::paintGL()
{
    glClear(GL_COLOR_BUFFER_BIT);

    glMatrixMode( GL_MODELVIEW );
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glEnable( GL_BLEND );

    glLoadIdentity();

    //
    // Rotation
    //
    glRotatef(45,1.0,0.0,0.0);
    // rotation about Y axis
    glRotatef(45,0.0,1.0,0.0);
    // rotation about Z axis
    glRotatef(0,0.0,0.0,1.0);

    //
    // Draw all the cubes
    //
    const float s = 0.1f;
    const float translationY = 0.6f;

    for(int i = 0; i < state; i++)
    {
        Vector3 pos = boxs[i].getPosition();
        Vector3 dim = boxs[i].getDimension();

        drawCube(-s * pos.getX(), s * pos.getY() - translationY, s * pos.getZ(), dim.getX(), dim.getY(), dim.getZ(), colors[i]);
    }

    glFlush();
}

void GLWidget::nextState()
{
    state ++;
    if(state >= nbBoxs())
        state = nbBoxs() - 1;
    update();
}

void GLWidget::previousState()
{
    state --;
    if(state <= 0)
        state = 0;
    update();
}

void GLWidget::finalState()
{
    state = nbBoxs() - 1;
    update();
}

void GLWidget::startState()
{
    state = 0;
    update();
}

void GLWidget::resizeGL(int w, int h)
{
    glViewport(0, 0, (GLint)w, (GLint)w);
}

void GLWidget::drawCube(float x, float y, float z, float w, float h, float l, color c)
{
    glBegin(GL_QUADS);

    glColor4f(c.r, c.g, c.b, c.a);

    glVertex3f(x, y, z);
    glVertex3f(x + w, y, z);
    glVertex3f(x + w, y + h, z);
    glVertex3f(x, y + h, z);

    glVertex3f(x, y, z + l);
    glVertex3f(x + w, y, z + l);
    glVertex3f(x + w, y + h, z + l);
    glVertex3f(x, y + h, z + l);

    glVertex3f(x, y, z);
    glVertex3f(x, y, z + l);
    glVertex3f(x, y + h, z + l);
    glVertex3f(x, y + h, z);

    glVertex3f(x + w, y, z);
    glVertex3f(x + w, y, z + l);
    glVertex3f(x + w, y + h, z + l);
    glVertex3f(x + w, y + h, z);

    glVertex3f(x, y + h, z);
    glVertex3f(x, y + h, z + l);
    glVertex3f(x + w, y + h, z + l);
    glVertex3f(x + w, y + h, z);

    glVertex3f(x, y, z);
    glVertex3f(x, y, z + l);
    glVertex3f(x + w, y, z + l);
    glVertex3f(x + w, y, z);

    glEnd();
}
