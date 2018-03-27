#include "glwidget.h"

float rand_a_b(int a, int b)
{
    return (rand()%(b-a)+a) / 100.0f;
}

GLWidget::GLWidget(QWidget *parent):
    QGLWidget(parent),
    state(1),
    zoom(1.0f)
{

}

void GLWidget::init(std::vector<Box> _boxs)
{
    boxs = _boxs;
    qDebug() << "Size = " << boxs.size();
    state = boxs.size();

    // Display Boxs
    for(int i = 0; i < boxs.size(); i++)
    {
        std::stringstream ss;
        ss << boxs[i];
        qDebug() << QString::fromStdString(ss.str());
    }

    // Generate random colors
    for(int i = 0; i < boxs.size(); i++)
    {
        color c;
        c.r = rand_a_b(0, 100);
        c.g = rand_a_b(0, 100);
        c.b = rand_a_b(0, 100);
        c.a = 0.5f;
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
    // rotation about X axis
    glRotatef(45,1.0,0.0,0.0);
    // rotation about Y axis
    glRotatef(-45,0.0,1.0,0.0);
    // rotation about Z axis
    glRotatef(0,0.0,0.0,1.0);

    //
    // Draw all the cubes
    //

    for(int i = 0; i < state; i++)
    {
        Vector3 pos = boxs[i].getPosition();
        Vector3 dim = boxs[i].getDimension();

        drawCube(pos.getX()*zoom, pos.getY()*zoom-0.5f, pos.getZ()*zoom, dim.getX()*zoom, dim.getY()*zoom, dim.getZ()*zoom, colors[i]);
    }

    glFlush();
}

void GLWidget::nextState()
{
    state ++;
    if(state >= nbBoxs())
        state = nbBoxs();
    update();
}

void GLWidget::previousState()
{
    state --;
    if(state <= 1)
        state = 1;
    update();
}

void GLWidget::finalState()
{
    state = nbBoxs();
    update();
}

void GLWidget::startState()
{
    state = 1;
    update();
}

void GLWidget::resizeGL(int w, int h)
{
    glViewport(0, 0, (GLint)w, (GLint)w);
}

void GLWidget::keyPressEvent(QKeyEvent *event)
{
    float coeff;
    if(zoom >= 0.1f)
        coeff = 0.1f;
    else
        coeff = 0.01f;
    if(event->key() == Qt::Key_I)
    {
        zoom -= coeff;
    }
    if(event->key() == Qt::Key_U)
    {
        zoom += coeff;
    }
    qDebug() << "Zoom = " << zoom;
    update();
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
