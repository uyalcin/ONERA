#include "glwidget.h"

GLWidget::GLWidget(QWidget *parent):
    QGLWidget(parent)
{

}

float rand_a_b(int a, int b)
{
    return (rand()%(b-a)+a) / 100.0f;
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

    glLoadIdentity( );

    //
    // Rotation
    //
    glRotatef(45,1.0,0.0,0.0);
    // rotation about Y axis
    glRotatef(45,0.0,1.0,0.0);
    // rotation about Z axis
    glRotatef(0,0.0,0.0,1.0);

    float s = 0.1f;
    for(int x = 0; x < 5; x++)
    {
        for(int y = 0; y < 5; y++)
        {
            for(int z = 0; z < 5; z++)
            {
                 drawCube(-s * x, s * y, s * z, s, s, s);
            }
        }

    }
    //drawCube(0, 0, 0, s, s, s);
    glFlush();
}

void GLWidget::resizeGL(int w, int h)
{
    //glViewport(0, 0, (GLint)w, (GLint)h);
}

void GLWidget::drawCube(float x, float y, float z, float w, float h, float l)
{
    glBegin(GL_QUADS);

    //glColor4f(  1.0,  0.0,  1.0 , 0.5f);
    glColor4f(rand_a_b(0, 100), rand_a_b(0, 100), rand_a_b(0, 100), 0.5f);
    glVertex3f(x, y, z);
    glVertex3f(x + w, y, z);
    glVertex3f(x + w, y + h, z);
    glVertex3f(x, y + h, z);

    //glColor4f(  1.0,  0.0,  1.0 , 0.5f);
    glVertex3f(x, y, z + l);
    glVertex3f(x + w, y, z + l);
    glVertex3f(x + w, y + h, z + l);
    glVertex3f(x, y + h, z + l);

    //glColor4f(   0.0,  1.0,  0.0 , 0.5f);
    glVertex3f(x, y, z);
    glVertex3f(x, y, z + l);
    glVertex3f(x, y + h, z + l);
    glVertex3f(x, y + h, z);

    //glColor4f(   0.0,  0.0,  1.0 , 0.5f);
    glVertex3f(x + w, y, z);
    glVertex3f(x + w, y, z + l);
    glVertex3f(x + w, y + h, z + l);
    glVertex3f(x + w, y + h, z);

    //glColor4f(   0.0,  1.0,  1.0, 0.5f );
    glVertex3f(x, y + h, z);
    glVertex3f(x, y + h, z + l);
    glVertex3f(x + w, y + h, z + l);
    glVertex3f(x + w, y + h, z);

    //glColor4f(   1.0,  0.0,  0.0 , 0.5f);
    glVertex3f(x, y, z);
    glVertex3f(x, y, z + l);
    glVertex3f(x + w, y, z + l);
    glVertex3f(x + w, y, z);

    glEnd();
}
