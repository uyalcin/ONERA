#ifndef GLWIDGET_H
#define GLWIDGET_H

#include <QGLWidget>
#include <GL/gl.h>
#include <GL/glu.h>

class GLWidget : public QGLWidget
{
    Q_OBJECT
public:
    explicit GLWidget(QWidget *parent = 0);

    void initializeGL();
    void paintGL();
    void resizeGL(int w, int h);

    // Draw a Cube
    void drawCube(float x, float y, float z, float w, float h, float l);
};

#endif // GLWIDGET_H
